from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ToDoItem(models.Model):
	description = models.CharField(max_length=256, null=False)
	done = models.BooleanField(null=False, default=False)
	created_time = models.TimeField(null=False, auto_now_add=True)
	pomodoros = models.IntegerField(null=False)