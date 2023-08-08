from django.db import models

# Create your models here.

class Rahbarlar(models.Model):
    uz_ism_familiya = models.CharField(max_length=255)
    ru_ism_familiya = models.CharField(max_length=255,null=True,blank=True)
    img=models.ImageField(upload_to="rahbarlar/",null=True,blank=True)
    uz_lavozim = models.CharField(max_length=255)
    ru_lavozim = models.CharField(max_length=255,null=True,blank=True)
    en_lavozim = models.CharField(max_length=255,null=True,blank=True)

    telefon = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)

    uz_qabul_qilish = models.CharField(max_length=555)
    ru_qabul_qilish = models.CharField(max_length=555,null=True,blank=True)
    en_qabul_qilish = models.CharField(max_length=555,null=True,blank=True)

    def __str__(self):
        return self.uz_ism_familiya


class Ishlar(models.Model):
    nomi = models.CharField(max_length=355)
    manzil = models.CharField(max_length=355)
    talablar = models.TextField()
    contact = models.CharField(max_length=255)
    maosh = models.CharField(max_length=555,null=True,blank=True)
    mudat = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomi

class Ariza(models.Model):
    ish = models.ForeignKey(Ishlar,on_delete=models.CASCADE)
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    yoshi = models.IntegerField()
    staj = models.CharField(max_length=255)
    ishchi_haqida = models.TextField(null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class New(models.Model):
    uz_title = models.CharField(max_length=999)
    # ru_title = models.CharField(max_length=999)
    # en_title = models.CharField(max_length=999)

    uz_text = models.TextField()
    # ru_text = models.TextField()
    # en_text = models.TextField()
    video = models.FileField(upload_to='news/',null=True,blank=True)
    img = models.ImageField(upload_to='news/',null=True,blank=True)
    img_2 = models.ImageField(upload_to='news/',null=True,blank=True)
    img_3 = models.ImageField(upload_to='news/',null=True,blank=True)


    uz_text_2 = models.TextField(null=True,blank=True)
    # ru_text_2 = models.TextField(null=True,blank=True)
    # en_text_2 = models.TextField(null=True,blank=True)

    uz_text_3 = models.TextField(null=True,blank=True)
    # ru_text_3 = models.TextField(null=True,blank=True)
    # en_text_3 = models.TextField(null=True,blank=True)

    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.uz_title

class Hududlar(models.Model):
    img = models.ImageField(upload_to='hududlar/')
    manzil = models.CharField(max_length=255)
    aholi = models.BigIntegerField(default=0)
    maydoni = models.CharField(max_length=255)
    loyhalar_soni = models.IntegerField(default=0)
    ish_joyi_soni = models.BigIntegerField(default=0)

    def __str__(self):
        return self.manzil



class BaholashMezon(models.Model):
    OTM_nomi = models.CharField(max_length=555)
    biriktirilgan_masul = models.CharField(max_length=555)
    kelganligi = models.IntegerField(default=0)
    tekshirish = models.BooleanField()

    def __str__(self):
        return self.OTM_nomi

class Baholash(models.Model):
    nomi = models.CharField(max_length=555)
    oquv_ishlari = models.IntegerField()
    yoshlar = models.IntegerField()
    ishlab_chiqarish = models.IntegerField()
    moliyaviy = models.IntegerField()
    xojalik = models.IntegerField()
    talim_sifati = models.IntegerField()
    ijro_intizomi = models.IntegerField()
    jazo = models.IntegerField()
    
    def __str__(self):
        return self.nomi
