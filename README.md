# Person API

The Person API allows you to manage information about individuals. You can create, retrieve, update, and delete person records using this API.

## Table of Contents

1. [Setup](#setup)
2. [Usage](#usage)

## Setup
To set up and run the Person API locally, follow these steps:

### Prerequisites
- Python 3.x
- pip
- Virtual environment (recommended)

### Clone the Repository
git clonehttps://github.com/PatrickNaenae/PersonApi.git
cd person-api

### Create a Virtual Environment (Optional but Recommended)
python -m venv venv.

### Activate the Virtual Environment
- On Windows:
venv\Scripts\activate.

- On macOS and Linux:
source venv/bin/activate.

### Install Dependencies
pip install -r requirements.txt.

### Set Up the Database
python manage.py migrate.

### Run the Development Server
python manage.py runserver.

## Usage
You can interact with the Person API by making HTTP requests to the provided endpoints. The API supports JSON data format for requests and responses.


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
        "email": "jane.doe@example.com"
    }
    ```

#### `DELETE /api/{user_id}`

- **Description**: Delete a person.
- **Request**: None
- **Response**:
  - Status: 204 No Content