#Code for Rest Api with Flask
from flask import Flask , jsonify, request
app = Flask(__name__)

users = {}

@app.route("/users",methods=["GET"])
def show_users():
    return jsonify(users),200

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users:
        return jsonify({"message": f"{username} already exists"}), 409

    users[username] = password
    return jsonify({"message": f"{username} registered successfully"}), 201

@app.route("/update",methods=['PUT'])
def update():
    data = request.get_json()
    username = data.get("username")
    new_password = data.get("password")
    
    if not username or not new_password:
       return jsonify({"error": "Both username and new password are required"}), 400

    if username not in users:
        return jsonify({"message": "User not found"}), 404

    users[username] = new_password
    return jsonify({"message": "Password updated successfully"}), 200
    

@app.route("/delete", methods=['DELETE'])
def delete():
    data = request.get_json()
    username = data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username not in users:
        return jsonify({"message": "User not found"}), 404

    del users[username]
    return jsonify({"message": f"{username} deleted successfully"}), 200
        
if __name__ == '__main__':
   app.run(debug = True)
