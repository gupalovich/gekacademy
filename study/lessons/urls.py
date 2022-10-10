from django.urls import path

from .views import CourseView


app_name = 'lessons'

urlpatterns = [
    path('<slug:course_slug>/', view=CourseView.as_view(), name='course')
]
