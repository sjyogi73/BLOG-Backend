from flask import Flask, jsonify
import hashlib
import mysql.connector
from dbconnect import connect_database

app = Flask(__name__)

# Perform POST operation
def post_data(data):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            data = data.json

            if not data:
                return jsonify({'error': 'No data provided'}), 400

            # Map JSON keys to table columns
            username = data.get('username')
           # password =data.get('password')
            password = hashlib.sha256(data.get('password').encode()).hexdigest()
            age = int(data.get('age'))
            gender = data.get('gender')
            status = data.get('status')
            
           # sql = "INSERT INTO user_details (username, password, age, createdDate, lastModifyed, active, gender, status) VALUES (%s, %s, %s, NOW(), NOW(), %s, %s, %s)"
           # cursor.execute(sql, ('test', 'test', 20, 0, 23, 0))
            
            sql = "INSERT INTO USER(username, password, age, createdDate, lastModifyed, gender, status) VALUES (%s, %s, %s, NOW(), NOW(), %s, %s)"
            cursor.execute(sql, (username, password, age, gender, status))
            conn.commit()
            return jsonify({'message': 'User details added successfully'}), 201
      
        except mysql.connector.Error as err:
            print("Error:", err.title)
            return jsonify({'error': err.title}), 500
    else:
        return jsonify({'error': 'Connection to database failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
