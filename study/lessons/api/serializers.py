from rest_framework import serializers

from ..models import Course, Lesson, Exercise


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['uuid', 'title', 'slug', 'status']

        extra_kwargs = {
            'url': {'view_name': 'api:course-list', 'lookup_field': 'uuid'}
        }
