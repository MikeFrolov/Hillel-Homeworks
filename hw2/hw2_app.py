from flask import Flask
from faker import Faker
import re

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


if __name__ == '__main__':
    app.run(debug=True)
