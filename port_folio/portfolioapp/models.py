from django.db import models


# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=30,default='',null=True,blank=True)
    img=models.ImageField(upload_to='media')
    upld_dt=models.DateTimeField(auto_now_add=True)   # type: ignore
    @staticmethod
    def get_all_photos():
        return Image.objects.all()  # type: ignore
    
class About(models.Model):
    image=models.ImageField(upload_to='personal',null=True,blank=True)
    title=models.CharField(max_length=50 ,null=True,blank=True)
    regular=models.TextField(null=True,blank=True)
    wrk=models.TextField( null=True,blank=True)
    techno=models.TextField(null=True,blank=True)
    hstry=models.TextField(null=True,blank=True)
    @staticmethod
    def get_all_details():
        return About.objects.all()
    
class Tutorial(models.Model):
    tutname=models.CharField(max_length=200)
    urlf=models.URLField()
    
    @staticmethod
    def get_all_values():
        return Tutorial.objects.all()
    
    def __str__(self):
        return self.tutname
        
class Inf(models.Model):
    info=models.TextField(null=True,blank=True)
    
    @staticmethod
    def get_all_infor():
        return Inf.objects.all()
class Etc(models.Model):
    passion_name=models.CharField(max_length=50)
    passion_url=models.URLField(null=True,blank=True)
    
    def __str__(self):
        return self.passion_name
    
    @staticmethod
    def get_all_etc():
        return Etc.objects.all()
class Singing(models.Model):
    sname=models.TextField()
    
    def __str__(self):
        return self.sname
    @staticmethod
    def get_all_content():
        return Singing.objects.all()

class Principle(models.Model):
    desc=models.TextField(null=True, blank=True)
    
class Contact(models.Model):
    name=models.CharField(max_length=30,default=True,)# type: ignore
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(default=0,null=True,blank=True)
    suggest=models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.name
    
