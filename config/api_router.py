from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from study.users.api.views import UserViewSet
from study.lessons.api.views import CourseViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('users', UserViewSet)
router.register('courses', CourseViewSet)


app_name = 'api'
urlpatterns = router.urls
