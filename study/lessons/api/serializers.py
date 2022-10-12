from rest_framework.serializers import ModelSerializer

from ..models import Course, Lesson, Exercise


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'uuid', 'title', 'slug', 'status']

        extra_kwargs = {
            'url': {'view_name': 'api:course-detail', 'lookup_field': 'uuid'}
        }


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'url',
            'uuid',
            'course',
            'title',
            'slug',
            'theory',
            'status',
            'created',
            'modified',
        ]
        depth = 1  # field nested depth

        extra_kwargs = {
            'url': {'view_name': 'api:lesson-detail', 'lookup_field': 'uuid'}
        }


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        depth = 1
