from rest_framework.serializers import ModelSerializer, UUIDField

from ..models import Course, Lesson, Exercise


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'uuid', 'title', 'slug', 'status']

        extra_kwargs = {
            'url': {'view_name': 'api:course-detail', 'lookup_field': 'uuid'}
        }


class LessonSerializer(ModelSerializer):
    course_uuid = UUIDField(source='course.uuid')

    class Meta:
        model = Lesson
        fields = [
            'url',
            'uuid',
            'course_uuid',
            'title',
            'slug',
            'theory',
            'status',
            'created',
            'modified',
        ]

        extra_kwargs = {
            'url': {'view_name': 'api:lesson-detail', 'lookup_field': 'uuid'}
        }


class ExerciseSerializer(ModelSerializer):
    lesson_uuid = UUIDField(source='lesson.uuid')

    class Meta:
        model = Exercise
        fields = [
            'url',
            'uuid',
            'lesson_uuid',
            'difficulty',
            'created',
            'modified',
        ]
        depth = 1

        extra_kwargs = {
            'url': {'view_name': 'api:exercise-detail', 'lookup_field': 'uuid'}
        }
