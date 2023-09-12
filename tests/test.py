import requests

BASE_URL = 'http://localhost:8000/api/person/' 

# Create
person_data = {
    "first_name": "Mark",
    "last_name": "Essien",
    "email": "mark.essien@example.com"
}
response = requests.post(BASE_URL, json=person_data)


if response.status_code == 201:
    print("Person created successfully")
else:
    print(f"Error creating person. Status code: {response.status_code}")

# Read
response = requests.get(BASE_URL + '15/')  

if response.status_code == 200:
    print("Person details fetched successfully")
else:
    print(f"Error fetching person details. Status code: {response.status_code}")

# Update
updated_data = {
    "first_name": "Mark",
    "last_name": "Essien",
    "email": "updated.email@example.com"
}
response = requests.put(BASE_URL + '15/', json=updated_data) 
print(response.content)

if response.status_code == 200:
    print("Person details updated successfully")
else:
    print(f"Error updating person details. Status code: {response.status_code}")

# Delete
response = requests.delete(BASE_URL + '15/')  

if response.status_code == 204:
    print("Person deleted successfully")
else:
    print(f"Error deleting person. Status code: {response.status_code}")
