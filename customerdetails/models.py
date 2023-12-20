from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	
	
 


	def __str__(self):
		return (self.email)