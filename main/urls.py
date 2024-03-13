from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'queries', QueryModelViewSet, basename='queries')
router.register(r'classes', ClassModelViewSet, basename='classes')

urlpatterns = [
    path("say_hello/", say_hello),
    path("profile/", user_profile),
    path("query/<int:id>/", filter_queries),
    path('', include(router.urls)),
    path("queries/", QueryView.as_view(), name="query-view"),
    path("schedules/filter/", fetch_class_schedule),
    path("schedule/create/", create_class_schedule),
]