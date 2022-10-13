from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Course, Lesson, Exercise
from .serializers import CourseSerializer, LessonSerializer, ExerciseSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.published().prefetch_related('lessons')
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
    queryset = Lesson.objects.published().select_related('course')
    serializer_class = LessonSerializer
    lookup_field = 'uuid'

    @action(detail=True)
    def exercises(self, request, *args, **kwargs):
        """Загрузить exercises относящиейся к Lesson; Url name - api:lesson-exercises"""
        instance = self.get_object()
        exercise_qs = instance.exercises.all()
        serializer = ExerciseSerializer(exercise_qs, many=True, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
