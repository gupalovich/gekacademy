from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin

from ..models import Course, Lesson, Exercise
from .serializers import CourseSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'uuid'
