from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Sales(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Transaction_date = db.Column(db.String(60), unique=True, nullable=False)
    Product = db.Column(db.String(60), unique=False, nullable=False)
    Price = db.Column(db.String(80), unique=False, nullable=False)
    Payment_Type = db.Column(db.String(40), unique=False, nullable=False)

    def __repr__(self):
        return '<Customers %r>' % self.first_name


if __name__ == '__main__':
    app.run(debug=True)
