from flask import Flask, request
import requests
import sqlite3
import string
import random

app = Flask(__name__)


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters
    password = ''

    for i in range(length):
        password += random.choice(choices)

    return password


@app.route('/')
def hello_world():
    """
    ?name=Dima&age=28
    """
    length = int(request.args.get('length') or 10)
    name = request.args.get('name', 'DEFAULT')
    age = request.args.get('age', 'DEFAULT_AGE')
    return f'{name} {age}, here is your password {generate_password(length)}'


@app.route('/exp/')
def exp():
    return 'exp'


@app.route('/encrypt-message/')
def encrypt_message_router():
    message = request.args['message']
    return encrypt_message(message)


@app.route('/space/')
def space():
    response = requests.get('http://api.open-notify.org/astros.json')
    num = response.json()['number']
    return str(num)


#### USERS/PHONES

@app.route('/users/list/')
def users_list():

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/create/')
def users_create():

    first_name = request.args['firstName']
    last_name = request.args['lastName']
    is_student = int(request.args['isStudent'] == 'true')  # true or false
    ID = random.randint(1, 100_000)  #todo

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO users VALUES ({ID}, '{first_name}', '{last_name}', {is_student});"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/phones/list/')
def phones_list():

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM phones;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/phones/')
def users_phones():

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.first_name, users.last_name, users.id, phones.value
        FROM users
        INNER JOIN phones ON phones.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)

####### HW-5########

@app.route('/emails/create/')
def emails_create():

    mail = request.args['mail']
    user_id = request.args['user_id']

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO emails VALUES (null, '{mail}', '{user_id}');"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"

@app.route('/emails/list/')
def emails_list():

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM emails;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)

@app.route('/emails/update/')
def emails_update():
    mail = request.args['mail']
    user_id = request.args['user_id']

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"" \
                f"UPDATE emails" \
                f" SET mail = '{mail}'" \
                f" WHERE user_id = '{user_id}';" \
                f""
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/emails/delete/')
def emails_delete():
    user_id = request.args['user_id']

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"" \
                f"DELETE FROM emails" \
                f" WHERE user_id = '{user_id}';"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/users/emails/')
def users_emails():

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.first_name, users.last_name, users.id, emails.mail
        FROM users
        INNER JOIN emails ON emails.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005', debug=True)

"""
OneToOne
OneToMany
ManyToMany
CRUD
C - create
R - read
U - update
D - delete???
"""