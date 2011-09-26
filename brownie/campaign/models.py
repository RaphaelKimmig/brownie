from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return  self.name
