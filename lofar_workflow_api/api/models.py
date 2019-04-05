from django.db import models
from jsonfield import JSONField

class Session(models.Model):
    # Properties describing the user
    email = models.CharField(max_length=255, default = "")
    description = models.CharField(max_length=1000, default = "")

    # Pipeline properties
    pipeline = models.CharField(max_length=100)
    config = JSONField() #config
    observation = models.CharField(max_length=100000)

    # Properties set by the API
    pipeline_version = models.CharField(max_length=100)
#    status = models.CharField(max_length = 20, \
#        choices=(("unknown", "unknown"), ("started", "started"), ("failure", "failure") ), \
#        default = "unknown")
    status = models.CharField(max_length = 20, \
                          choices=(("Waiting", "Waiting"), ("Running", "Running"), ("Success", "Success"), ("Cancelled", "Cancelled"),  ("PermanentFailure", "PermanentFailure"), ("SystemError", "SystemError"), ("TemporaryFailure", "TemporaryFailure")), \
                          default = "Waiting")
    pipeline_response = models.CharField(max_length = 1000, default = "")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    di_image = models.ImageField(upload_to='images')

    def __str__(self):
        return "Printing Session object containing: Pipeline={}, Email={}, config={}, date_created={}, description={}".format(self.pipeline, self.email, self.config, self.date_created, self.description)
