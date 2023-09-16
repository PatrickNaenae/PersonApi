# Person API Documentation

# Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
   - [Create Person](#create-person)
   - [Get Person Details](#get-person-details)
   - [Update Person Details](#update-person-details)
   - [Delete Person](#delete-person)
3. [Sample Usage](#sample-usage)
4. [Limitations and Assumptions](#limitations-and-assumptions)
5. [Setup](#setup)
6. [Deployment](#deployment)


## Introduction

This API allows users to manage person records along with their associated addresses. It supports basic CRUD (Create, Read, Update, Delete) operations.

## Endpoints

### Person

#### `GET /api`

- **Description**: Retrieve a list of all persons.
- **Request**: None
- **Response**:
  - Status: 200 OK
  - Body:
    ```json
    [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "age": 27,
            "email": "john.doe@example.com"
        },
        ...
    ]
    ```

#### `GET /api/{user_id}`

- **Description**: Retrieve details of a specific person.
- **Request**: None
- **Response**:
  - Status: 200 OK
  - Body:
    ```json
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "email": "john.doe@example.com"
    }
    ```

#### `POST /api`

- **Description**: Create a new person.
- **Request**:
  - Body:
    ```json
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
  - Status: 201 Created
  - Body:
    ```json
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "email": "john.doe@example.com"
    }
    ```

#### `PUT /api/{user_id}`

- **Description**: Update details of an existing person.
- **Request**:
  - Body:
    ```json
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 27,
        "email": "Johndoee@gmail.com"
    }
    ```
- **Response**:
  - Status: 200 OK
  - Body:
    ```json
    {
        "id": 1,
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 27,
        "email": "jane.doe@example.com"
    }
    ```

#### `DELETE /api/{user_id}`

- **Description**: Delete a person.
- **Request**: None
- **Response**:
  - Status: 204 No Content

#### `GET /api/?name={full_name}`
- **Description**: Retrieve details of a specific person by name.
- **Request**: None
- **Response**:
- Status: 200 OK
- Body:
```json
Copy code
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "age": 27,
    "email": "john.doe@example.com"
}
```

#### `GET /api/?age={age}`
- **Description**: Retrieve a list of persons by age.
- **Request**: None
- **Response**:
- Status: 200 OK
- Body:
```json
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "email": "john.doe@example.com"
    },
    ...
]
```

#### `GET /api/?email={email}`
- **Description**: Retrieve a list of persons by email.
- **Request**: None
- **Response**:
- Status: 200 OK
- Body:
```json
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "email": "john.doe@example.com"
    },
    ...
]
```

#### `GET /api/{user_id}/?name={full_name}`
- **Description**: Retrieve details of a specific person by name with ID.
- **Request**: None
- **Response**:
- Status: 200 OK
- Body:
```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "age": 27,
    "email": "john.doe@example.com"
}
```

#### `PUT /api/{user_id}/?name={full_name}`
- **Description**: Update details of an existing person by name with ID.
- **Request**:
- Body:
```json
{
    "first_name": "Jane",
    "last_name": "Doe",
    "age": 27,
    "email": "jane.doe@example.com"
}
```
- **Response**:
- Status: 200 OK
- Body:
```json
{
    "id": 1,
    "first_name": "Jane",
    "last_name": "Doe",
    "age": 27,
    "email": "jane.doe@example.com"
}
```

#### `DELETE /api/{user_id}/?name={full_name}`
- **Description**: Delete a person by name with ID.
- **Request**: None
- **Response**:
- Status: 204 No Content

## Limitations and Assumptions
- The API does not handle authentication and authorization for simplicity.
- Error handling is basic and may not cover all edge cases.

## Setup
Follow these steps to set up and run the API locally:
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Apply the migrations using `python manage.py migrate`.
5. Start the development server with `python manage.py runserver`.

## Deployment
To deploy this API on a server, you can follow these general steps:

1. Set up a server environment (e.g., pythonanywhere, Heroku, etc.).
2. Configure the server with the necessary dependencies (Python, Django, etc.).
3. Clone the repository to the server.
4. Set up a web server (e.g., Nginx, etc.) to handle incoming requests.
5. Configure the server to run the Django application.

Please note that specific deployment steps may vary depending on your chosen server environment.

