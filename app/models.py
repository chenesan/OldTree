from __future__ import unicode_literals

from django.db import models

class Tree(models.Model):
    age = models.IntegerField(default=-1) #expect_tree_age
    url = models.URLField() #pic_url
    latitude = models.FloatField() #treea_addr['latitude']
    longtitude = models.FloatField() #treea_addr['longtitude']
    chest = models.FloatField() #tree_chest
    height = models.FloatField() #tree_height
    type = models.CharField(max_length=20) #type_cht_name
    division = models.CharField(max_length=20) #treea_addr['admin_division_name']
    address = models.CharField(max_length=200) #treea_addr['detail_treea_addr']
    id = models.IntegerField(primary_key=True) #treea_addr['old_tree_serial_no']

class Message(models.Model):
    content = models.TextField()
