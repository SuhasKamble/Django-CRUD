from django.db import models

# Create your models here.
class Info(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.fname
