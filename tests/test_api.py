# from rest_framework import status
# from rest_framework.test import APITestCase
# from person.models import Person, Address
# from person.serializers import PersonSerializer
# from django.shortcuts import get_object_or_404
# import random
# import string

# class TestPersonAPI(APITestCase):

#     def setUp(self):
#         def generate_random_string(length):
#             letters = string.ascii_letters
#             return ''.join(random.choice(letters) for i in range(length))

#         unique_email = f"{generate_random_string(8)}@example.com"

#         self.person_data = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "email": unique_email  
#         }
#         self.person = Person.objects.create(**self.person_data)
#         self.update_data = {
#         "first_name": "Jane",
#         "last_name": "Doe",  
#         "email": "jane.doe@example.com"
#         }
#         self.url = f"/api/person/{self.person.id}/"

#     def test_create_person(self):
#         url = "/api/person/"
#         response = self.client.post(url, self.person_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_read_person(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_person(self):
#         response = self.client.put(self.url, self.update_data, format='json')
#         print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_person(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


