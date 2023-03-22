from django.db import models

from modality.models import Modality


class Activity(models.Model):

    code = models.CharField(max_length=5)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    workload_min = models.IntegerField()
    workload_max = models.IntegerField()
    use = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.code)
