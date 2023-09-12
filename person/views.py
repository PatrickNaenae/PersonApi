from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        age = self.request.query_params.get('age')
        email = self.request.query_params.get('email')

        if name:
            first_name, last_name = name.split()
            return Person.objects.filter(first_name=first_name, last_name=last_name)
        else:
            queryset = Person.objects.all()

            if age:
                queryset = queryset.filter(age=age)

            if email:
                queryset = queryset.filter(email=email)

            return queryset
