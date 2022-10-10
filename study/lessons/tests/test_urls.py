from django.urls import resolve, reverse

from ..models import Course, Lesson, Exercise


def test_course(course: Course):
    course_reverse = reverse('lessons:course', kwargs={'course_slug': course.slug})
    course_resolve = resolve(f'/sub/{course.slug}/').view_name
    assert course_reverse == f'/sub/{course.slug}/'
    assert course_resolve == 'lessons:course'


def test_lesson(lesson: Lesson):
    lesson_reverse = reverse(
        'lessons:lesson',
        kwargs={'course_slug': lesson.course.slug, 'lesson_slug': lesson.slug})
    lesson_resolve = resolve(f'/sub/{lesson.course.slug}/{lesson.slug}/').view_name
    assert lesson_reverse == f'/sub/{lesson.course.slug}/{lesson.slug}/'
    assert lesson_resolve == 'lessons:lesson'
