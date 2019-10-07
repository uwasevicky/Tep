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
class Payment (models.Model):
	home = models.ForeignKey(Home, on_delete = models.CASCADE)
	fees = models.IntegerField()
	description = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	paymentMethod = models.CharField()
	transctionNo = models.ForeignKey(Transction, on_delete = models.CASCADE)
class Transction(models.Model):
	fees = models.IntegerField()
	termN0 =models.ForeignKey(Term, on_delete = models.CASCADE)
	date =models.DateField()
	time =models.TimeField()
class Term(models.Model):
	fees = models.IntegerField()
	status = models.CharField(max_length=10)
	Year = models.IntegerField()

		

		