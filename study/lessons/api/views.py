from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Course, Lesson, Exercise
from .serializers import CourseSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'uuid'

    @action(detail=True)
    def lessons(self, request, *args, **kwargs):
        """Загрузить lessons относящиейся к Course"""
        pass
