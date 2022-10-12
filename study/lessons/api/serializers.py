from rest_framework import serializers

from ..models import Course, Lesson, Exercise


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'uuid', 'title', 'slug', 'status']

        extra_kwargs = {
            'url': {'view_name': 'api:course-detail', 'lookup_field': 'uuid'}
        }


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('id', 'course', )
