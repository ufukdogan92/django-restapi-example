from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



class Patients(models.Model):
    patient_name = models.CharField(max_length=25)
    patient_lname = models.CharField(max_length=25)
    patient_email = models.EmailField(max_length=40)
    patient_GENDER = (('K', 'Kadin'),('E', 'Erkek'))
    patient_gender = models.CharField(choices=patient_GENDER, max_length=1)
    patient_phone = models.CharField(max_length=20)


    def __unicode__(self):
        return self.patient_name + " " + self.patient_lname
    class Meta:
        verbose_name ="Hasta Profili"
        verbose_name_plural="Hasta Profilleri"


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=25)
    doctor_lname = models.CharField(max_length=25)
    doctor_email = models.EmailField(max_length=40)
    doctor_GENDER = (('K', 'Kadin'),('E', 'Erkek'))
    doctor_gender = models.CharField(choices=doctor_GENDER, max_length=1)
    doctor_phone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.doctor_name + " " + self.doctor_lname
    class Meta:
        verbose_name ="Doktor Profili"
        verbose_name_plural="Doktor Profilleri"