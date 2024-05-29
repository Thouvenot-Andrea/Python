from bottle import Bottle, run, template, request, redirect
import mysql.connector

app = Bottle()


# Configuration de la base de données
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="Andrea",
        password="HelioS@@du26",
        database="Bottle"
    )
    return conn


@app.route('/')
def index():
    #connection à la BDD
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('view/index', users=users)


@app.route('/add', method='GET')
def add_user_form():
    return '''
        <form action="/add" method="post">
            Name: <input name="name" type="text" />
            Age: <input name="age" type="text" />
            <input value="Add" type="submit" />
        </form>
    '''


@app.route('/add', method='POST')
def add_user():
    # Pour obtenir les données du formulaire
    name = request.forms.get('name')
    age = request.forms.get('age')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


@app.route('/delete/<id:int>', method='GET')
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


if __name__ == "__main__":
    run(app, host='localhost', port=8080)
