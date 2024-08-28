from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length = 50)
    
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=50, choices=[("User", "User"), ("Admin","Admin")], default="User")
    group = models.ManyToManyField(Group, related_name="user")
    

