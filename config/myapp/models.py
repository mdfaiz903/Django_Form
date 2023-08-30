from django.db import models

# Create your models here.
class geekmodel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    
class info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=25)
    email =models.EmailField()
    roll = models.IntegerField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    texarea = models.TextField()
    checkbox = models.CharField(max_length=20)
    payment = models.DecimalField(max_digits=6,decimal_places=2)
    django = models.BooleanField()
    # file = models.FileField(upload_to='images/')
    def __str__(self):
        return self.first_name