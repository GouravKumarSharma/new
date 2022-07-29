from django.db import models

# Create your models here.
class Markets(models.Model):
    market_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.market_name

class table(models.Model):
    market_name = models.ForeignKey(Markets, on_delete=models.CASCADE)
    jodi = models.IntegerField(max_length=10)
    release_date = models.DateField()
    panel = models.IntegerField(max_length=10)
    card = models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.market_name)

class Adpost(models.Model):
    id = models.BigAutoField(primary_key=True)
    heading=models.CharField(max_length=200)
    post = models.CharField(max_length=2000)
    active=models.BooleanField(default=False)
    def __str__(self):
        return str(self.heading)

class jduser(models.Model):
    userid = models.IntegerField(max_length=200,primary_key=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.userid)

class jdpost(models.Model):
    userid = models.ForeignKey(jduser, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    time = models.DateField()
    rank = models.IntegerField(max_length=2)
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.username)


class jdregister(models.Model):
    userid = models.IntegerField(max_length=200,primary_key=True)
    password = models.CharField(max_length=50)
    username =  models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return str(self.username)

class contectform(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField()
    message =  models.CharField(max_length=200)
    mobile = models.IntegerField(max_length=2)
    def __str__(self):
        return str(self.name)
