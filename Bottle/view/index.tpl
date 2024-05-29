<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
</head>
<body>
<h1>User List</h1>
<ul>
    % for user in users:
    <li>{{user['name']}} {{user['age']}} - <a href="/delete/{{user['id']}}">Delete</a></li>
    % end
</ul>
<a href="/add">Add User</a>
</body>
</html>
