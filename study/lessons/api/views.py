from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Course, Lesson, Exercise
from .serializers import CourseSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'uuid'
