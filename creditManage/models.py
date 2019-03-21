from django.db import models

# Create your models here.
class user_detail(models.Model):
	name=models.CharField(max_length=32)
	email=models.CharField(max_length=30)
	phone=models.IntegerField()
	age=models.IntegerField()
	gender=models.CharField(max_length=6)
	credit=models.IntegerField( )
	
	def __str__(self):
		return self.name


class transaction(models.Model):
	trac_from=models.CharField(max_length=32)
	trac_to=models.CharField(max_length=32)
	credit=models.IntegerField()

	def __str__(self):
		return self.trac_from
