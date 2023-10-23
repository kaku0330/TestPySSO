from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    UserID = models.CharField(db_column = 'UserID', primary_key = True, unique = True, max_length = 32)
    Name = models.CharField(db_column = 'Name', unique = False, max_length = 64)
    Password = models.CharField(db_column = 'Password', max_length = 48)
    IP = models.CharField(db_column = 'IP', unique = False, max_length = 15)
    Browser = models.CharField(db_column = 'Browser', unique = False, max_length = 10)

    class Meta:
        db_table = 'user'