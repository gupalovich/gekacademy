from django.urls import resolve, reverse

from ..models import Course, Lesson, Exercise


def test_course_list(course: Course):
    rev = reverse('api:course-list')
    res = resolve('/api/courses/').view_name
    assert rev == '/api/courses/'
    assert res == 'api:course-list'


def test_course_detail(course: Course):
    rev = reverse('api:course-detail', kwargs={'uuid': course.uuid})
    res = resolve(f'/api/courses/{course.uuid}/').view_name
    assert rev == f'/api/courses/{course.uuid}/'
    assert res == 'api:course-detail'


def test_course_lessons(course: Course):
    rev = reverse('api:course-lessons', kwargs={'uuid': course.uuid})
    res = resolve(f'/api/courses/{course.uuid}/lessons/').view_name
    assert rev == f'/api/courses/{course.uuid}/lessons/'
    assert res == 'api:course-lessons'
