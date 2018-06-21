from django.db import models

# Create your models here.
class Session(models.Model):
	name = models.CharField(max_length=255, blank=False, unique=False)
	# observation = models.ForeignKey('Observation', 
	# 	related_name = 'sessions', 
	# 	on_delete=models.CASCADE)
	# 	#models.IntegerField(default=0)
	# pipeline_conf = models.ForeignKey('PipelineConfiguration', 
	# 	related_name = 'sessions', 
	# 	on_delete=models.CASCADE)
	# owner = models.ForeignKey('auth.User',
	# 	related_name = 'sessions', 
	# 	on_delete = models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)

# class PipelineConfiguration(models.Model):
# 	# owner = models.ForeignKey('auth.User', related_name = 'pipelineconfigurations', on_delete= models.CASCADE)
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	date_modified = models.DateTimeField(auto_now=True)

# 	name = models.CharField(max_length=255, blank=False, unique=False)
# 	some_setting_1 = models.FloatField(default=0)
# 	some_setting_2 = models.FloatField(default=0)

# 	def __str__(self):
# 		return "{}".format(self.name)


# class Observation(models.Model):
# 	# owner = models.ForeignKey('auth.User', related_name = 'observation', on_delete= models.CASCADE)
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	date_modified = models.DateTimeField(auto_now=True)

# 	name = models.CharField(max_length=255, blank=False, unique=False)
# 	some_identifier = models.CharField(max_length=255, blank=False, unique=False)

# 	def __str__(self):
# 		return "{}".format(self.name)