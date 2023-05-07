from django.db import models

# Create your models here.

class Rahbarlar(models.Model):
    ism_familiya = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    qabul_qilish = models.CharField(max_length=555)
    
    def __str__(self):
        self.ism_familiya


class Ishlar(models.Model):
    nomi = models.CharField(max_length=355)
    manzil = models.CharField(max_length=355)
    talablar = models.TextField()
    contact = models.CharField(max_length=255)
    namuna_cv = models.FileField(upload_to='example_cv/')

    def __str__(self):
        return self.nomi

class Ariza(models.Model):
    ish = models.ForeignKey(Ishlar,on_delete=models.CASCADE)
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    yoshi = models.IntegerField()
    staj = models.CharField(max_length=255)
    ishchi_haqida = models.TextField(null=True,blank=True)
    cv = models.FileField(upload_to='cv/',null=True,blank=True)
    
    def __str__(self):
        return f"{self.ism} {self.familiya}"

