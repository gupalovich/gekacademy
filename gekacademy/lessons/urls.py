from django.urls import path

from .views import CourseListView, LessonListView, ExerciseDetailView


app_name = 'lessons'

urlpatterns = [
    path('<slug:course_slug>/', view=CourseListView.as_view(), name='course'),
    path('<slug:course_slug>/<slug:lesson_slug>/', view=LessonListView.as_view(), name='lesson'),
    path(
        '<slug:course_slug>/<slug:lesson_slug>/<uuid:exercise_uuid>/',
        view=ExerciseDetailView.as_view(),
        name='exercise'),
]
