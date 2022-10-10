from django.urls import resolve, reverse

from ..models import Course, Lesson, Exercise


url_prefix = '/learn'


def test_course(course: Course):
    rev = reverse('lessons:course', kwargs={'course_slug': course.slug})
    res = resolve(f'{url_prefix}/{course.slug}/').view_name
    assert rev == f'{url_prefix}/{course.slug}/'
    assert res == 'lessons:course'


def test_lesson(lesson: Lesson):
    rev = reverse(
        'lessons:lesson',
        kwargs={'course_slug': lesson.course.slug, 'lesson_slug': lesson.slug})
    res = resolve(f'{url_prefix}/{lesson.course.slug}/{lesson.slug}/').view_name
    assert rev == f'{url_prefix}/{lesson.course.slug}/{lesson.slug}/'
    assert res == 'lessons:lesson'


def test_exercise(exercise: Exercise):
    url = '%s/%s/%s/%s/' % (
        url_prefix,
        exercise.lesson.course.slug,
        exercise.lesson.slug,
        exercise.uuid)
    rev = reverse(
        'lessons:exercise',
        kwargs={
            'course_slug': exercise.lesson.course.slug,
            'lesson_slug': exercise.lesson.slug,
            'exercise_uuid': exercise.uuid,
        })
    assert rev == url
    assert resolve(url).view_name == 'lessons:exercise'
