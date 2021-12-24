from django.db import models

class DefaultListing(models.Model):
    name                        = models.CharField(max_length=100)
    price                       = models.IntegerField()
    description                 = models.CharField(max_length=500)
    brand                       = models.CharField(max_length=100)

class SwitchListing(models.Model):
    listing                     = models.ForeignKey(DefaultListing, on_delete=models.CASCADE)
    switch_type                 = models.CharField(max_length=100)
    switch_bottom_out           = models.CharField(max_length=100)
    switch_actuation_force      = models.CharField(max_length=100)
    switch_stem_compatibility   = models.CharField(max_length=100)
