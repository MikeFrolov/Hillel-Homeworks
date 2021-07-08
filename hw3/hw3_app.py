from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Sales(db.Model):  # DB Model

    id = db.Column(db.Integer, primary_key=True)
    Transaction_date = db.Column(db.String(60), unique=False)
    Product = db.Column(db.String(60), unique=False)
    Price = db.Column(db.String(80), unique=False)
    Payment_Type = db.Column(db.String(40), unique=False)

    def __repr__(self):
        return '<Sales %r>' % self.Transaction_date


db.create_all()  # Create DB

with open("homework3sales.csv") as file:  # Writing data to the database
    rows = csv.reader(file, delimiter=';')
    selling = []
    for row in rows:
        selling.append(row)
    for i, note in enumerate(selling[1:]):
        rec_to_db = Sales(Transaction_date=note[0],
                          Product=note[1],
                          Price=note[2],
                          Payment_Type=note[3]
                          )
        db.session.add(rec_to_db)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
