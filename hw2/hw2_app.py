from flask import Flask
from faker import Faker
import re
import csv
import requests

app = Flask(__name__)


@app.route("/")
def home_page() -> str:
    return "<p>Welcome to HW2 Home Page!</p>"


@app.route("/requirements")
def req_file() -> str:
    with open('requirements.txt') as file:
        lines = file.read()
        return f"<p>{lines}</p>"


@app.route("/generate-users/<number>", methods=['GET'])
def user_gen(number) -> dict:
    fake = Faker()
    users = {}
    for i in range(int(number)):
        user = fake.name()
        pattern = re.compile(r'\w+')
        name = pattern.findall(user)[0]
        mail = fake.email()
        users[name] = mail

    return users


@app.route("/mean")
def average_values() -> str:

    height_sm, weight_sm = [], []

    with open('hw2/hw.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            height_sm.append(float(row[' "Height(Inches)"']))
            weight_sm.append(float(row[' "Weight(Pounds)"']))

    medium_h = 2.54 * sum(sorted(height_sm)) / len(height_sm)
    medium_w = 0.453592 * sum(sorted(weight_sm)) / len(weight_sm)

    return f"<p>Medium height: {medium_h}sm, Medium weight: {medium_w}kg</p>"


@app.route("/space")
def astronauts() -> str:
    r = requests.get('http://api.open-notify.org/astros.json')
    number = r.json()["number"]
    return f"<p>{number}</p>"

    return a.number


if __name__ == '__main__':
    app.run(debug=True)
