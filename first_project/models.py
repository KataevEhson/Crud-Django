from django.db import models


class Tesks(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    due_date = models.CharField(max_length=100)


