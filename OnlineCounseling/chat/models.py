from django.db import models


# Create your models here.

class Text_Message(models.Model):
    user_id = models.CharField(max_length=22)
    message = models.CharField(max_length=500, default='')
    dt_time = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user_id + "  " + self.message