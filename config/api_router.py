from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from study.users.api.views import UserViewSet
from study.lessons.api.views import CourseViewSet, LessonViewSet, ExerciseViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('users', UserViewSet, basename='user')
router.register('courses', CourseViewSet, basename='course')
router.register('lessons', LessonViewSet, basename='lesson')
router.register('exercises', ExerciseViewSet, basename='exercise')


app_name = 'api'
urlpatterns = router.urls
