from flask import Flask, jsonify
import mysql.connector
from dbconnect import connect_database

app = Flask(__name__)

# Perform PUT operation
def put_data(data):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()
            data = data.json

            if not data:
                return jsonify({'error': 'No data provided'}), 400

           # Map JSON keys to table columns
            username = data.get('username')
            password =data.get('password')
            age = data.get('age')
            active = data.get('active')
            gender = data.get('gender')
            status = data.get('status')
            sql = "UPDATE USER SET"
            if password !="":
                sql += " password = '{}',".format(password)
            
            if age !=0:
                sql += " age = {},".format(age)
            
            if active == 0 or active == 1 :
                sql += " active = {},".format(active)

            if gender !="":
                sql += " gender = '{}',".format(gender)

            if status !=0:
                sql += " status = {},".format(status)
            
            # Remove the trailing comma and add the WHERE clause
            sql = sql.rstrip(', ') + " WHERE username = '{}'".format(username)
            print(sql)
            cursor.execute(sql)

            #sql = """UPDATE USER SET password = %s, age = %s, lastModifyed = NOW(), active = %s, gender = %s, status = %s WHERE username = %s """
            #cursor.execute(sql, (password, age, active, gender, status,username))
            conn.commit()
            return jsonify({'message': 'User details added successfully'}), 201
      
        except mysql.connector.Error as err:
            print("Error:", err)
            return jsonify({'error': 'Database error'}), 500
    else:
        return jsonify({'error': 'Connection to database failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
