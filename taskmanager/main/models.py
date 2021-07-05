from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=100)
    text = models.TextField('Text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
