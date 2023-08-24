Project Description: Real-Time Cryptocurrency Price Tracker with Flask

This project is a real-time cryptocurrency price tracking web application built using Python and Flask, allowing users to monitor the latest prices of various cryptocurrencies. It consists of two main components: a Flask web application and a data collection script that retrieves cryptocurrency price data from the Binance API and stores it in an SQLite database.

Key Features:

    Cryptocurrency Price Tracking: Users can access real-time prices of cryptocurrencies such as Bitcoin (BTC), Ethereum (ETH), and others.

    Detailed Currency Information: Users can click on individual currency symbols to view detailed information, including historical price data.



To run the Flask web application and the data collection script together, follow these steps:
Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

Python 3: Make sure you have Python 3 installed on your system.

Flask: You can install Flask using pip if you haven't already.

    pip install Flask

Binance API Python SDK: Install the Binance API Python SDK using pip.

    pip install python-binance

Setting up the SQLite Database

    Create an SQLite database file named currency.db in the same directory as your Python scripts. You can use the SQLite command-line tool or a SQLite GUI like DB Browser for SQLite to create the database.

    Create a table named currency with columns symbol, price, and time. You can use the following SQL command to create the table:

    CREATE TABLE currency (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        price REAL,
        time DATETIME
    );

Configuration

    Replace "BINANCE_API_KEY" and "BINANCE_API_SECRET" with your actual Binance API key and secret in the script where you initialize the Binance client.

Running the Application

Now, you can run the Flask web application and the data collection script.

    1.)Open a terminal and navigate to the directory containing your Python scripts.

    2.)Run the Flask application by executing the app.py script. Make sure you have saved your Flask application code in a file named app.py.

-python app.py

This will start the Flask web server, and your web application will be accessible at http://localhost:5000/.

In a separate terminal, run the data collection script by executing the pars.py script.

    python pars.py

    This script collects data from Binance and inserts it into the SQLite database at regular intervals.

Accessing the Web Application

You can access the web application by opening a web browser and navigating to http://localhost:5000/. This will display the list of currencies and their prices.

To access detailed information about a specific currency, you can visit URLs like http://localhost:5000/BTCUSDT or http://localhost:5000/ETHUSDT, replacing the symbol with the currency symbol you want to view.

Please note that this setup is for development and testing purposes. For a production environment, you should consider deploying your Flask application on a production server and securing your API keys properly.
