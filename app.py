from flask import Flask,request
from routes.Login.getUser import get_data
from routes.Login.postUser import post_data
from routes.Login.putUser import put_data
from routes.Login.deleteUser import delete_data

app = Flask(__name__)

# Perform GET operation
@app.route('/v1/user/get/<username>', methods=['GET'])
def data(username):
   return get_data(username)

# Perform POST operation
@app.route('/v1/user/post', methods=['POST'])
def postData():
   return post_data(request)

# Perform PUT operation
@app.route('/v1/user/put', methods=['PUT'])
def putData():
   return put_data(request)

# Perform DELETE operation
@app.route('/v1/user/delete/<name>', methods=['DELETE'])
def deteleData(name):
   return delete_data(name)  

if __name__ == '__main__':
    app.run(debug=True)
