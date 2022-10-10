from django.urls import resolve, reverse

from ..models import Course, Lesson, Exercise


url_prefix = '/api'


def test_course_list(course: Course):
    rev = reverse('api:course-list')
    res = resolve(f'/api/courses/').view_name
    assert rev == f'/api/courses/'
    assert res == 'api:course-list'
