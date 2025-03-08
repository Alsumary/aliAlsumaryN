from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class home(models.Model):
    title = models.CharField(max_length=50)
    personalImage = models.CharField(max_length=1500, default="https://lh3.googleusercontent.com/drive-viewer/AKGpihYOZsaMEyC0OCUZK9MDbH-6pS0L4bbc8JIFVAGVdUCl-wu275ocp6fEPSW3gJU5Seecl_NPwcNSyZttQ8seijhTtVeU39jcNw=s1600-rw-v1")
    smallContent = models.TextField(max_length=2000)
class abouts(models.Model):
    TitleText = models.CharField(max_length=50)
    personalImage = models.CharField(max_length=1500, default="https://lh3.googleusercontent.com/drive-viewer/AKGpihZywZtaaSEZ4A1rQqLZH_MBMnKemFTDwvQcNLtgdFcv2M5zkxAGqFTQPh7hJwq11Q-C-toJHtupsV2792rGTs60MIA86rySKA=s1600-rw-v1")
    aboutme = models.TextField(max_length=2000)
    counterOneName = models.CharField(max_length=30)
    counterOneNumber = models.IntegerField(default=0)
    counterTwoName = models.CharField(max_length=30)
    counterTwoNumber = models.IntegerField(default=0)
    counterThreeName = models.CharField(max_length=30)
    counterThreeNumber = models.IntegerField(default=0)
class information(models.Model):
    emailAddress = models.EmailField()
    instaAcc = models.CharField(max_length=1000)
    whatsNumber = models.CharField(max_length=1000)
    linkedinAcc = models.CharField(max_length=1000)
    facebookAcc = models.CharField(max_length=1000)
    logo = models.CharField(max_length=4000, default="Nothing")

class skills(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"
    
class experience(models.Model):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    sort_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title}"
    
class education(models.Model):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    sort_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title}"

class gallerys(models.Model):
    pageTitle = models.CharField(max_length=30,db_index=True,default='Imagination Trumps Knowledge!')
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    visitLink = models.TextField(max_length=2500, default='1')
    photo = models.TextField(max_length=2500, default='https://i.imgur.com/DzlrvEa.jpeg')
    fullWidth = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
class clients(models.Model):
    Logolink = models.TextField(max_length=2500)
    MainLogo = models.BooleanField(default=False)

class bts(models.Model):
    header = models.TextField(max_length=200, default="Behind The Scenes")
    photoLink = models.TextField(max_length=2500)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"
