from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "date_modified")

admin.site.register(Course, CourseAdmin, ClassShedule, ClassAttendance, Query, QueryComment)
