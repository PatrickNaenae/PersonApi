import requests

BASE_URL = 'http://127.0.0.1:8000/api/'  


def test_create_person():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

    response = requests.post(BASE_URL, json=data)

    assert response.status_code == 201


def test_get_person():
    response = requests.get(BASE_URL + '3/')  
    print(response.content)

    assert response.status_code == 200
    assert response.json()["first_name"] == "John"


def test_update_person():
    data = {
        "first_name": "John",
        "last_name": "Smith",
        "age": 31,
        "email": "john.smith@example.com"
    }

    response = requests.put(BASE_URL + '3/', json=data)  

    assert response.status_code == 200
    assert response.json()["last_name"] == "Smith"


def test_delete_person():
    response = requests.delete(BASE_URL + '3/')  

    assert response.status_code == 204


if __name__ == "__main__":
    test_create_person()
    test_get_person()
    test_update_person()
    test_delete_person()
