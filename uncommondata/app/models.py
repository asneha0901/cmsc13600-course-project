from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    ROLE_CHOICES = [
        ('harvester', 'Harvester'),
        ('curator', 'Curator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

#The UserType table will have just two options: Harvester and Curator. 
#The User is formed with django's automatic user package and if a user is deleted, then the type is also deleted. The def(str) is just for when we want to see it

class Institution(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class ReportingYear(models.Model):
    year = models.CharField(max_length=9) 

    def __str__(self):
        return self.year
    
class Upload(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    reporting_year = models.ForeignKey(ReportingYear, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.institution} {self.reporting_year} upload by {self.uploaded_by.username}"

#The uploads table allows users (linked with a foreign key) to add files to the app while making sure that 
#each upload links to a user, institution and reporting year (which is the metadata hw3 seems to be referring to!)

class Facts(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    reporting_year = models.ForeignKey(ReportingYear, on_delete=models.CASCADE)
    source_upload = models.ForeignKey(Upload, on_delete=models.SET_NULL, null=True)
    fact_title = models.CharField(max_length=255)
    fact_vale = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.institution} {self.reporting_year} | {self.field_name}"

