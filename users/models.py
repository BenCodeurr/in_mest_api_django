from django.db import models
# from django.contrib.auth.models import AbstractUser

class IMUser (models.Model):
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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Cohort (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='N/A')
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
