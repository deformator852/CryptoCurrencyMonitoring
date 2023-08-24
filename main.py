from flask import Flask, render_template
import sqlite3
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("currency.db")
    cur = conn.cursor()
    currencies = cur.execute("SELECT symbol,price,time FROM currency;")
    return render_template("index.html",currencies=currencies)

@app.route("/<symbol>")
def get_info_about_currency(symbol):
    conn = sqlite3.connect("currency.db")
    cur = conn.cursor()
    currency_info = cur.execute(f"SELECT price,time FROM currency WHERE symbol = '{symbol}' ORDER BY time DESC;")
    return render_template("currency.html",title=symbol,currency_info=currency_info,symbol=symbol)


if __name__ == "__main__":
    app.run()
