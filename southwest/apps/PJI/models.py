from django.db import models
from localflavor.us.us_states import US_STATES
# Create your models here.
class Franchise(models.Model):
	name = models.CharField(max_length=300)
	dev_id = models.IntegerField(blank=True, null=True)
	focus_group = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Store(models.Model):
	franchise = models.ForeignKey('Franchise', related_name='stores')
	store_id = models.IntegerField(max_length=6)
	name = models.CharField(max_length=300)
	tgm_store = models.BooleanField(default=False)
	address_1 = models.CharField(max_length=500)
	address_2 = models.CharField(max_length=500, blank=True, null=True)
	state = models.CharField(max_length=2, choices=US_STATES)
	zip_code = models.IntegerField(max_length=5)

	def __unicode__(self):
		return "%d: %s" % (self.store_id, self.name)
