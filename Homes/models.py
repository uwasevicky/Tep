from django.db import models

# Create your models here.
class home(models.Model):
	Nid =models.IntegerField(max_length=50)
	DateOfBirth=models.DateField()
	FirstName=models.CharField(max_length=250)
	LastName=models.CharField(max_length=250)
	Phone1=models.IntegerField()
	Status=models.CharField(max_length=10)
	Address=models.CharField(max_length=250)
	MaritalStatus=models.CharField(max_length=45)
	Phone2=models.IntegerField()
	Email=models.EmailField(max_length=250)
	Village=models.CharField(max_length=50)
class= notification(models.Model):
	Phone = models.IntegerField()
	text = models.CharField(max_length=500)
	Type = models.CharField(max_length=250)
	Date = models.DateField()
	Time = models.TimeField()
class transfers (models.Model): 
	homeid = models.ForeignKey(home, on_delete=models.CASCADE)
	From  =models.CharField(max_length=10)
	To =models.CharField(max_length=10)
	Date =models.DateField(max_length=10)
	Time = models.TimeField(max_length=10)
	status =models.CharField(max_length=10)
