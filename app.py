from flask import Flask, jsonify

app = Flask(__name__)

# Sample in-memory "database"
users = [
    {"user_id": 1, "username": "jdoe", "email": "jdoe@example.com"},
    {"user_id": 2, "username": "asmith", "email": "asmith@example.com"}
]

# Endpoint to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["user_id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
