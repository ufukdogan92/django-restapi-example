from django.contrib.auth.models import User, Group
from hastaTakip.hastaTakipApi.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patients
        fields = ('url', 'patient_name','patient_lname','patient_email','patient_gender','patient_phone')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctors
        fields = ('url', 'doctor_name','doctor_lname','doctor_email','doctor_gender','doctor_phone')

