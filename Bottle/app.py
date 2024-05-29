import sqlite3
from bottle import route, run, debug, template, request, static_file, error


@route('/todo')
@route('/my_todo_list')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '0'")
    result = c.fetchall()
    c.close()
    output = template('view/make_table', rows=result)

    return output


@route('/new', method="GET")
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the Id is %s</p>' % new_id
    else:
        return template('view/new_task.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('view/edit_task', old=cur_data, no=no)


# dans la barre de recherche après 8080/  il faut mettre item puis l'id de l'item ex http://127.0.0.1:8080/item1
# affiche : Task: Read A-byte-of-python to get a good introduction into Python
@route('/item<item:re:[0-9]+>')
def show_item(item):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]


@route('/help')
def help():
    return static_file('help.html', root='/path/to/file')


# pareil à la route item
@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}


# afficher message d'erreur pour les pages qui n'existe pas
@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
