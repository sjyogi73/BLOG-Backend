from flask import Flask, jsonify
import mysql.connector
from dbconnect import connect_database
app = Flask(__name__)

# Perform GET operation
def get_data(username):
    conn = connect_database()

    if conn is not None:
        if username != '0':
            sql = "SELECT * FROM USER WHERE username = '{}'".format(username)
        else:
            sql = "SELECT * FROM USER"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            data = [{'userId': row[0], 'userName': row[1], 'password': row[2], 'age': row[3], 'createdDate': row[4], 'lastModifyed': row[5], 'active': row[6], 'gender': row[7]} for row in rows]
           
            return jsonify({'data': data}), 200
        except mysql.connector.Error as err:
            print("Error:", err)
            return jsonify({'error': 'Database error'}), 500
    else:
        return jsonify({'error': 'Connection to database failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
