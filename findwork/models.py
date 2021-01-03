from django.db import models
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

    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=GENDER, max_length=1)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
 

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='Use', on_delete=models.CASCADE) 
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
    documents = models.ImageField(default='img.jpg')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title 
