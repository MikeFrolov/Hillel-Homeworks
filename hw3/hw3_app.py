from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
import csv
import os


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


def db_creator():
    db.create_all()  # Create DB

    with open("homework3sales.csv") as file:  # Writing data to the database
        csv_rows = csv.reader(file, delimiter=';')
        selling = []
        for row in csv_rows:
            selling.append(row)
        for note in sorted(selling[1:]):
            rec_to_db = Sales(Transaction_date=note[0],
                              Product=note[1],
                              Price=note[2],
                              Payment_Type=note[3]
                              )
            db.session.add(rec_to_db)
        db.session.commit()


if not os.path.exists('hw3.db'):  # If not table 'Sales'
    db_creator()


@app.route('/')
def index() -> str:
    return f'<p><h1>Home Work 3</h1></p>' \
           f'<p><h3>Flask + SQLAlchemy</h3></p>' \
           f'<p>...</p>' \
           f'<p><a href="/summary">Summary</a></p>' \
           f'<p><a href="/sales">Sales</a></p>'


@app.route("/summary")
def summary() -> dict:
    """
    We read the database line by line, enter the days from the date into the dictionary as a key,
    and prices into the value, if the key already exists, we increase the value by the price
    """
    day_price = {}

    data_reader = Sales.query.all()[1:]
    for data in data_reader:
        day = data.Transaction_date.split()[0]
        price = int(data.Price)
        if day not in day_price:
            day_price[day] = price
        else:
            day_price[day] += price

    return OrderedDict(sorted(day_price.items()))


@app.route('/sales')
def sales() -> dict:
    product = request.args.get('product')
    payment_type = request.args.get('payment_type')
    product_payment_filter = {}

    data_reader = Sales.query.all()
    for data in data_reader:
        content = [
            data.Transaction_date,
            data.Product,
            data.Price,
            data.Payment_Type]

        if not product and data.Payment_Type == payment_type:
            product_payment_filter[data.id] = str([*content])
        elif data.Product == product and not payment_type:
            product_payment_filter[data.id] = str([*content])
        if data.Product == product and data.Payment_Type == payment_type:
            product_payment_filter[data.id] = str([*content])

    return product_payment_filter


if __name__ == '__main__':
    app.run(debug=True)
