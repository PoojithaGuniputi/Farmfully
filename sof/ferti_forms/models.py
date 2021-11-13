from django.db import models

# crops=['rice','maize','chickpea']
# Create your models here.
class FertilizerData(models.Model):   
    # cropname=models.CharField(max_length=30)
    crop=models.CharField(max_length=30,default="rice")
    # crop=models.CharField(max_length=1,choices=crops)
    nitrogen=models.IntegerField()
    potassium=models.IntegerField()
    phosphorous=models.IntegerField()

    def __str__(self):
         return self.crop