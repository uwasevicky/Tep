from django.db import models

# Create your models here.
class Province(models.Model):
	Name = models.CharField(max_length=100)
	Address = models.CharField(max_length=150)
	Phone = models.IntegerField()
	Email = models.EmailField()
class District(models.Model):
	districtName = models.CharField(max_length=50)
	districtAddress = models.CharField(max_length=50)
	districtPhone= models.IntegerField()
	districtEmail = models.EmailField()
	province = models.ForeignKey(Province, on_delete=models.CASCADE)

class Sector(models.Model):
	sectorName = models.CharField(max_length=100)
	sectorAddress= models.CharField(max_length=150)
	sectorPhone = models.IntegerField()
	sectorEmail = models.EmailField()
	district = models.ForeignKey(District, on_delete = models.CASCADE)

class Cells (models.Model):
	cellName = models.CharField(max_length=100)
	cellAddress =models.CharField(max_length=150)
	cellEmail =models.EmailField()
	cellPhone =models.IntegerField()
