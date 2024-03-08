from flask import Flask, jsonify
import mysql.connector
from dbconnect import connect_database
app = Flask(__name__)

# Perform GET operation
def get_data(User,Key):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM USER WHERE username = '{}' and password = '{}'".format(User,Key)
            cursor.execute(sql)
            rows = cursor.fetchall()

            # Check if the result set is not empty
            if rows:
                print("Rows are not empty:")
                return jsonify({'result': 'Login success'}), 200
            else:
                print("No rows found.")
                return jsonify({'result': 'Login failed'}), 200
            
        except mysql.connector.Error as err:
            print("Error:", err)
            return jsonify({'error': err}), 500
    else:
        return jsonify({'error': 'Connection to database failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
