# User Profile API

A simple RESTful API for managing user profiles, built with Flask. The API supports basic CRUD operations: Create, Read, Update, and Delete users.

## Features

- Retrieve all users (`GET /users`)
- Retrieve a specific user by ID (`GET /users/<user_id>`)
- Create a new user (`POST /users`)
- Update an existing user (`PUT /users/<user_id>`)
- Delete a user (`DELETE /users/<user_id>`)

## Installation

To set up and run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Jon-109/user-profile-api.git
   cd user-profile-api

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Flask app:

   ```bash
   python app.py

## Usage

Use Postman or `curl` to interact with the API. Below are the available endpoints:

---

### Endpoints

#### Retrieve All Users

**GET** `/users`

Example Response:
```json
[
    {
        "user_id": 1,
        "username": "jdoe",
        "email": "jdoe@example.com"
    },
    {
        "user_id": 2,
        "username": "asmith",
        "email": "asmith@example.com"
    }
]

#### Retrieve a User by ID

**GET** `/users/<user_id>`

Example:
```bash
curl http://127.0.0.1:5000/users/1


Example Response:
```json
{
    "user_id": 1,
    "username": "jdoe",
    "email": "jdoe@example.com"
}

Create a New User
**POST** `/users/<user_id>`

Request Body:
```json
{
    "username": "newuser",
    "email": "newuser@example.com"
}

Example:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com"}' http://127.0.0.1:5000/users

Example Response:
```json
{
    "user_id": 3,
    "username": "newuser",
    "email": "newuser@example.com"
}

Update an Existing User
**PUT** `/users/<user_id>`

Example:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"username": "updateduser", "email": "updated@example.com"}' http://127.0.0.1:5000/users/1

Request Body:
```json
{
    "username": "updateduser",
    "email": "updated@example.com"
}

Example Response:
```json
{
    "user_id": 1,
    "username": "updateduser",
    "email": "updated@example.com"
}

Delete a User
DELETE /users/<user_id>

Example:
```bash
curl -X DELETE http://127.0.0.1:5000/users/1

Example Response:
```json
{
    "message": "User with ID 1 has been deleted"
}

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is open source and available under the [MIT License](LICENSE).
