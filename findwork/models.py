from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser


GENDER = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)
JOB_TYPE = (
    ('fulltime', "Full time"),
    ('part_time', "Part time"),
    ('internship', "Internship"),
)
CATEGORY = (
    ('Web_development',"Web Development"),
    ('backend_development',"Backend Development"),
    ('api_development',"Api Development"),
    ('data_engineering',"Data Engineering"),
)

class User(AbstractUser):
    first_name= models.CharField(max_length=10, null=True)
    last_name= models.CharField(max_length=10, null=True)
    role = models.CharField(choices=ROLE,  max_length=10)
    profile= CloudinaryField(default='image.jpg')
    bio= models.CharField(max_length=50, default='get to know us')
    gender = models.CharField(choices=GENDER, max_length=5)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        return self.first_name
 

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='employer', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=15)
    category = models.CharField(choices=CATEGORY,max_length=30)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Application(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    documents = models.FileField(default='image.jpg')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title 
