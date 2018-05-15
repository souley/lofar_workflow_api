from django.db import models

# Create your models here.
class Session(models.Model):
	name = models.CharField(max_length=255, blank=False, unique=False)
	pipeline_id = models.IntegerField(default=0)
	obs_id = models.IntegerField(default=0)
	owner = models.ForeignKey('auth.User',
		related_name = 'sessions', 
		on_delete = models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)
