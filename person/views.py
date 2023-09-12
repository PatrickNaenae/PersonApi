# views.py
from rest_framework import viewsets, status
from .models import Person
from rest_framework.response import Response
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request):
        name = request.query_params.get('name')
        if name:
            first_name, last_name = name.split()  # Assuming the first and last name are separated by a space
            queryset = Person.objects.filter(first_name=first_name, last_name=last_name)
            serializer = self.get_serializer(queryset, many=True)
        else:
            serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            name = request.query_params.get('name')
            if name:
                first_name, last_name = name.split()  # Assuming the first and last name are separated by a space
                person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(person)
        return Response(serializer.data)

    def create(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({"detail": "Name is required in query parameter."}, status=status.HTTP_400_BAD_REQUEST)

        first_name, last_name = name.split()  # Assuming the first and last name are separated by a space
        data = request.data.copy()
        data['first_name'] = first_name
        data['last_name'] = last_name
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            name = request.query_params.get('name')
            if name:
                first_name, last_name = name.split()  # Assuming the first and last name are separated by a space
                person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            name = request.query_params.get('name')
            if name:
                first_name, last_name = name.split()  # Assuming the first and last name are separated by a space
                person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
            else:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def retrieve_by_name(self, request, name=None):
        try:
            person = Person.objects.get(pk=int(name))
        except (Person.DoesNotExist, ValueError):
            first_name, last_name = name.split()
            person = get_object_or_404(Person, first_name=first_name, last_name=last_name)

        serializer = self.get_serializer(person)
        return Response(serializer.data)

    def update_by_name(self, request, name=None):
        try:
            first_name, last_name = name.split()
            person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
        except ValueError:
            return Response({"detail": "Invalid name format. Use 'first_name last_name'."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy_by_name(self, request, name=None):
        try:
            first_name, last_name = name.split()
            person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
        except ValueError:
            return Response({"detail": "Invalid name format. Use 'first_name last_name'."}, status=status.HTTP_400_BAD_REQUEST)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
