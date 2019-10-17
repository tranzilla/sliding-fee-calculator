from django.db import models

# Create your models here.
class SlidingScale(models.Model):
    scale = models.CharField(max_length=1)
    fs_1 = models.IntegerField()
    fs_2 = models.IntegerField()
    fs_3 = models.IntegerField()
    fs_4 = models.IntegerField()
    fs_5 = models.IntegerField()
    fs_6 = models.IntegerField()
    fs_7 = models.IntegerField()
    fs_8 = models.IntegerField()

    def __str__(self):
        return self.scale
