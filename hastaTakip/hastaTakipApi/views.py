from django.contrib.auth.models import User

from rest_framework import viewsets
from hastaTakip.hastaTakipApi.serializers import *
from hastaTakip.hastaTakipApi.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer