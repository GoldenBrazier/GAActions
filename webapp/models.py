from django.db import models

# Create your models here.

class RegisrationData(models.Model):
    eljur_user_id = models.CharField(max_length=256, default='none')
    eljur_login = models.CharField(max_length=256, default='none')
    activation_phrase = models.CharField(max_length=512, default='none')
    expires = models.CharField(default="0", max_length=512)

class UserData(models.Model):
    yandex_user_id = models.CharField(max_length=256, default='none')
    eljur_user_id = models.CharField(max_length=256, default='none')
