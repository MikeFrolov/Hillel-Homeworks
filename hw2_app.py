from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page() -> str:
    return "<p>Welcome to HW2 Home Page!</p>"


@app.route("/requirements")
def req_file() -> str:
    with open('requirements.txt') as file:
        lines = file.read()
        return f"<p>{lines}</p>"


if __name__ == '__main__':
    app.run(debug=True)
