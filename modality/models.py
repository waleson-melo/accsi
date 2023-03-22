from django.db import models


class Modality(models.Model):

    name = models.CharField(max_length=15)
    description = models.TextField(max_length=255)


    def __str__(self):
        return "{}".format(self.name)
