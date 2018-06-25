from django.db import models

# Create your models here.
class Session(models.Model):
    # API specific properties: 
    name = models.CharField(max_length=255, blank=False, unique=False)
    status = models.CharField(max_length = 20, choices=(("unknown", "unknown"), ("running", "running"), ("finished", "finished")), default = "unknown")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Pipeline configuration properties:
    avg_freq_step = models.IntegerField(default=2) # minimum=0. maximum=1000 "AVG_TIME_STEP"
    avg_time_step = models.IntegerField(default=4) # minimum=0. maximum=1000 "AVG_TIME_STEP"
    do_demix = models.BooleanField(default=True) # "DO_DEMIX"
    demix_freq_step = models.IntegerField(default=2) #minimum=0. maximum=1000 "DEMIX_FREQ_STEP"
    demix_time_step = models.IntegerField(default=2) # "DEMIX_TIME_STEP"
    demix_sources = models.CharField(max_length=4, choices=(("CasA", "CasA"), ("CygA","CygA")), default="CasA") # "DEMIX_SOURCES"
    select_NL = models.BooleanField(default=True) #"SELECT_NL"
    parset = models.CharField(max_length=7, choices=\
        (("", ""), ("hba_npp", "hba_npp"), ("hba_raw", "hba_raw"), ("lba_npp", "lba_npp"), ("lba_raw", "lba_raw"))\
        , default = "lba_npp") # "PARSET"

    def __str__(self):
        return "{}".format(self.name)

# class PipelineConfiguration(models.Model):
#   # owner = models.ForeignKey('auth.User', related_name = 'pipelineconfigurations', on_delete= models.CASCADE)
#   date_created = models.DateTimeField(auto_now_add=True)
#   date_modified = models.DateTimeField(auto_now=True)

#   name = models.CharField(max_length=255, blank=False, unique=False)
#   some_setting_1 = models.FloatField(default=0)
#   some_setting_2 = models.FloatField(default=0)

#   def __str__(self):
#       return "{}".format(self.name)


# class Observation(models.Model):
#   # owner = models.ForeignKey('auth.User', related_name = 'observation', on_delete= models.CASCADE)
#   date_created = models.DateTimeField(auto_now_add=True)
#   date_modified = models.DateTimeField(auto_now=True)

#   name = models.CharField(max_length=255, blank=False, unique=False)
#   some_identifier = models.CharField(max_length=255, blank=False, unique=False)

#   def __str__(self):
#       return "{}".format(self.name)