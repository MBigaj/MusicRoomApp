from django.db import models
import string
import random


def generate_unique_code():
    length = 8
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0: # Check whether the code already exists in our database
            break

    return code


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default='', unique=True) # Unique key to join a session
    host = models.CharField(max_length=50, unique=True) # Unique single host method
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True) # Automatically add date and time of addition