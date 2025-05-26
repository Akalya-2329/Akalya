from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    email=models.EmailField()


    

    def __str__(self):
        return (self.name)
    
class biodata(models.Model):
    dept=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    stream=models.CharField(max_length=50)

    def __str__(self):
        return (self.mobile_no)





