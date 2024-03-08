from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Connect to MySQL database
def connect_database():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Connected to the database")
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None