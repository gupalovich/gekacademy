from django.urls import resolve, reverse

from ..models import Course, Lesson, Exercise


def test_course(course: Course):
    rev = reverse('lessons:course', kwargs={'course_slug': course.slug})
    res = resolve(f'/{course.slug}/').view_name
    assert rev == f'/{course.slug}/'
    assert res == 'lessons:course'
