from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    kid = models.CharField(max_length=100,null=True,blank=False,default="NONE")
    username = models.CharField(max_length=100,default="None")
    last_name = models.CharField(max_length=100,default="None")
    email = models.EmailField(blank=True,null=True,unique=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='default.png')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    phone=models.CharField(max_length=15,blank=True,null=True,default="none")
    def __str__(self):
        return str(self.email)
    


class Kids(models.Model):
    parent = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=10000,null=True,blank=True)
    age = models.CharField(max_length=10)
    group = models.CharField(max_length=10)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='default.png')
    full_name = models.CharField(max_length=100 ,unique=True)
    last_name = models.CharField(max_length=100)
    absente = models.IntegerField(blank=True,null=True)
    motivari = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return str(self.name)
class absente_elev(models.Model):
    owner = models.ForeignKey(Kids,on_delete=models.CASCADE,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    numar = models.IntegerField()
    data = models.CharField(max_length=100,blank=True,null=True)
class motivari_elev(models.Model):
    owner = models.ForeignKey(Kids,on_delete=models.CASCADE,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    numar = models.IntegerField()
    data = models.CharField(max_length=100,blank=True,null=True)
