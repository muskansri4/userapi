from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    permission = models.ForeignKey(Permission,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    firtsname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

