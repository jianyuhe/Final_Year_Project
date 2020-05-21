from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Location(models.Model):
    parkName = models.CharField(max_length=50)
    address = models.CharField(max_length=200)


class Feedback(models.Model):
    username = models.CharField(max_length=50)
    parkName = models.CharField(max_length=50)
    feedbk = models.CharField(max_length=6000)
