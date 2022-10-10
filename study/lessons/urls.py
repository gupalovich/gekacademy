from django.urls import path

from .views import CourseView, LessonView


app_name = 'lessons'

urlpatterns = [
    path('<slug:course_slug>/', view=CourseView.as_view(), name='course'),
    path('<slug:course_slug>/<slug:lesson_slug>/', view=LessonView.as_view(), name='lesson'),
]
