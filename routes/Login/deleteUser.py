from flask import Flask, jsonify
import mysql.connector
from dbconnect import connect_database

app = Flask(__name__)

# Perform Delete operation
def delete_data(username):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM USER WHERE username = %s"
            cursor.execute(sql, (username,))
           
            conn.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        except mysql.connector.Error as err:
            print("Error:", err)
            return jsonify({'error': 'Database error'}), 500
    else:
        return jsonify({'error': 'Connection to database failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
