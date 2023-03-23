from django.db import models


class Student(models.Model):

    registration = models.CharField('Matrícula', max_length=8)
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField()
    phone_number = models.CharField('Telefone', max_length=11)

    def __str__(self):
        return '{}'.format(self.name)
