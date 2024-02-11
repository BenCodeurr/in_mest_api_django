from django.db import models

class Course (models.Model):
    name = models.CharField(max_length=2000)
    description = models.TextField(default='N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"

class ClassShedule(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(default='N/A')
    start_date_and_time=models.DateTimeField()
    end_date_and_time=models.DateTimeField()
    is_repeated=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    repeat_frequency=models.IntegerField()
    organizer=models.CharField(max_length=50)
    cohort=models.ForeignKey('users.Cohort', on_delete=models.CASCADE)
    venue=models.CharField(max_length=100)

class ClassAttendance(models.Model):
    class_schedule=models.ForeignKey(ClassShedule, on_delete=models.CASCADE)
    attendee=models.ForeignKey('users.IMUser', on_delete=models.CASCADE)
    is_present=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True, null=True, blank=True)
    author=models.ForeignKey('users.IMUser', on_delete=models.CASCADE)

class Query(models.Model):
    RESOLUTION_STATUS = (
      (1, 'PENDING'),
      (2, 'IN_PROGRESS'),
      (3, 'DECLINED'),
      (4, 'RESOLVED'),
    )
    title=models.CharField(max_length=100)
    description=models.TextField(default='N/A')
    resolution_status=models.SmallIntegerField(choices=RESOLUTION_STATUS)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True, null=True, blank=True)
    author=models.ForeignKey('users.IMUser', on_delete=models.CASCADE)

class QueryComment(models.Model):
    query=models.ForeignKey(Query, on_delete=models.CASCADE)
    comment=models.TextField(default="N/A")
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True, null=True, blank=True)
    author=models.ForeignKey('users.IMUser', on_delete=models.CASCADE)