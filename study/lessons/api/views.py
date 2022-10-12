from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Course, Lesson, Exercise
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('lessons')
    serializer_class = CourseSerializer
    lookup_field = 'uuid'

    @action(detail=True)
    def lessons(self, request, *args, **kwargs):
        """Загрузить lessons относящиейся к Course; Url name - api:course-lessons"""
        instance = self.get_object()
        lessons_qs = instance.lessons.all()
        serializer = LessonSerializer(lessons_qs, many=True, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class LessonViewSet(ReadOnlyModelViewSet):
    queryset = Lesson.objects.select_related('course')
    serializer_class = LessonSerializer
    lookup_field = 'uuid'
