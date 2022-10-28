from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=20)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):return self.ism
class Mavzu(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    m_mavzu = models.CharField(max_length=30)
    matn = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):return self.sarlavha

