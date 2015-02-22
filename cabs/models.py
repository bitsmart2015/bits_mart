from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CabOffer(models.Model):
	user = models.ForeignKey(User)
	destination = models.CharField(max_length=40)
	# car = models.CharField(max_length=20)
	# city = models.CharField(max_length=200)
	seats = models.IntegerField(null=True,blank=True)
	# total_cost = models.IntegerField()
	date_of_travel = models.DateTimeField()
	closed=models.NullBooleanField(null=True,blank=True)
	phone = models.IntegerField(null=True,blank=True)
	def __unicode__(self):
		return str(self.user.username) + ' '+ str(self.destination)