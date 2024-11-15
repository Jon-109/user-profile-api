from flask import Flask, jsonify, request

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

# Single endpoint to add a new user (fixing the duplicate)
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()  # Get JSON data from the request

    # Validate that both 'username' and 'email' are provided
    if not new_user or "username" not in new_user or "email" not in new_user:
        return jsonify({"error": "Username and email are required"}), 400

    # Generate a new unique user_id based on the last user's ID
    new_user["user_id"] = users[-1]["user_id"] + 1 if users else 1
    users.append(new_user)  # Add the new user to the list

    # Return the newly created user with a 201 status code
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
