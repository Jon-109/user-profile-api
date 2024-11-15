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

if __name__ == '__main__':
    app.run(debug=True)
