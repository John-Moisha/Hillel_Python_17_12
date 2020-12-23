from flask import Flask, jsonify
from faker import Faker
import requests
import pandas as pd

fake = Faker()
app = Flask(__name__)

# 1. Возвращать содержимое файла с пайтон пакетами (requirements.txt) PATH: /requirements/ открыть файл requirements.txt и вернуть его содержимое
@app.route('/requierements/')
def req_file():
    df = open('requirements.txt', 'r')
    return df.read()

# 2. Вывести 100 случайно сгенерированных юзеров (почта + имя) 'Dmytro aasdasda@mail.com' PATH: /generate-users/ ( https://pypi.org/project/Faker/ ) + параметр который регулирует количество юзеров
@app.route('/generate-users/')

def gen_users():
    users = [''.join(fake.name() + fake.ascii_email()) for _ in range(100)]
    return jsonify(users)


# 3. Средний рост, средний вес (см, кг) (hw.csv) PATH: /mean/
@app.route('/mean/')
def mean():
    df = pd.read_csv('hw-2.csv')
    height = (df[' "Height(Inches)"'].sum() / len(df.index)) * 2.54
    weight = (df[' "Weight(Pounds)"'].sum() / len(df.index)) * 0.453592
    return 'Средний рост: ' + str(height) + ' см. ' + '<br>' + ' Средний вес: ' + str(weight) + ' Кг.'

# 4. Вывести количество космонавтов в настоящий момент (http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/) PATH: /space/
@app.route('/space/')
def space():
    cosmo = requests.get('http://api.open-notify.org/astros.json')
    r = cosmo.json()['number']
    return 'Космонавтов:' + str(r)


if __name__ == '__main__':
    app.run()