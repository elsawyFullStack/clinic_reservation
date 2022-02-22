from django.db import models
from django.contrib.auth.models import User

USER_TYPE_CHOICES = USER_TYPE = (('doctor', 'Doctor'), ('receptionist', 'Receptionist'), ('patient', 'Patient'))
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField('Profile Settings', max_length=15, choices=USER_TYPE_CHOICES, default='patient')
    user_mobile = models.IntegerField('Mobile', null=True)
    user_gender = models.CharField('Gender', max_length=10, choices=GENDER_CHOICES, default='male')

    def __str__(self):
        return str(self.user.username)
