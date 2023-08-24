from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from datetime import datetime
import sqlite3
import asyncio

API_KEY = "BINANCE_API_KEY"
API_SECRET = "BINANCE_API_SECRET"
client = Client(api_key=API_KEY, api_secret=API_SECRET)


async def pars():
    conn = sqlite3.connect("currency.db")
    cur = conn.cursor()
    while True:
        tickers = client.get_all_tickers()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for ticker in tickers:
            if ticker['symbol'] == f"BTCUSDT":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"ETHUSDT":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"ARBUSDT":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"LTCUSDT":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"OPTUSD":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"SOLUSDT":
                print(ticker['symbol'])
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
            if ticker['symbol'] == f"MATICUSDT":
                cur.execute("INSERT INTO currency (symbol, price, time) VALUES (?, ?, ?);",
                            (ticker['symbol'], ticker['price'], time))
                conn.commit()
        await asyncio.sleep(90)


asyncio.run(pars())
