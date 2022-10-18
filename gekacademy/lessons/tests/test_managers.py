from django.test import TestCase

from ..models import Course, Lesson
from .factories import CourseFactory, LessonFactory


class TestCourseManager(TestCase):
    def setUp(self):
        self.batch_size = 5
        CourseFactory.create_batch(size=self.batch_size, status='draft')
        CourseFactory.create_batch(size=self.batch_size, status='published')

    def test_published(self):
        qs_all = Course.objects.all()
        qs = Course.objects.published()

        assert len(qs_all) == self.batch_size * 2
        assert len(qs) == self.batch_size
        assert qs.first().status == 'published'
        assert qs.last().status == 'published'


class TestLessonManager(TestCase):
    def setUp(self):
        self.batch_size = 5
        LessonFactory.create_batch(size=self.batch_size, status='draft')
        LessonFactory.create_batch(size=self.batch_size, status='published')

    def test_published(self):
        qs_all = Lesson.objects.all()
        qs = Lesson.objects.published()

        assert len(qs_all) == self.batch_size * 2
        assert len(qs) == self.batch_size
        assert qs.first().status == 'published'
        assert qs.last().status == 'published'
