# Little Lemon API

## Introduction

Little Lemon API is a simple API that allows you to create, read, update and delete users and their posts. It is built with Python, Django, DRF and sqlite3.

## Installation

- [] Clone the repository
- [] Create a virtual environment and activate it with `python -m venv venv` and `source venv/bin/activate`
- [] Install the dependencies with `pip install -r requirements.txt`
- [] Run the server with `python manage.py runserver`

## Usage

### Users

- [] Create a user with `POST /users/` with the following body:

```
{
    "username": "username",
    "password": "password"
}
```

- [] Get all users with `GET /users/`

```json
[
  {
    "id": 1,
    "username": "username"
  },
  {
    "id": 2,
    "username": "username2"
  }
]
```

- [] Get a user with `GET /users/:id/`

```json
{
  "id": 1,
  "username": "username"
}
```

- [] Update a user with `PUT /users/:id/` with the following body:

```json
{
  "username": "new_username",
  "password": "new_password"
}
```

- [] Delete a user with `DELETE /users/:id/`

```json
{
  "id": 1,
  "username": "username"
}
```

### Posts

- [] Create a post with `POST /posts/` with the following body:

```json
{
  "title": "title",
  "body": "body",
  "user": 1
}
```
