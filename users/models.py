from django.db import models
from django.contrib.auth.models import AbstractUser

class IMUser (AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'EIT'),
      (2, 'TEACHING_FELLOW'),
      (3, 'ADMIN_STAFF'),
      (4, 'ADMIN'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    is_active = models.BooleanField(default = False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique = True, max_length = 50)
    username = None
    USERNAME_FIELD = 'email'
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Cohort (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    year = models.PositiveIntegerField(max_length=5)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

class CohortMember(models.Model):
    cohort=models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member=models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    author=models.ForeignKey(IMUser, on_delete=models.CASCADE)

# IMUser (first_name, last_name, is_active, user_type [EIT, TEACHING_FELLOW, ADMIN_STAFF, ADMIN], date_created). Feel free to add extra fields you can think of. Custom user  management/auth implementation will be done later
# Cohort(name, description, year, start_date, end_date, is_active, date_created, date_modified, author [should reference IMUser model])
# CohorMember(cohort[Should reference Cohort model], member [should reference IMUser], is_active, date_created, date_modified, author [should reference IMUser model])
