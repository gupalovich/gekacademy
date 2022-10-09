import re

from transliterate import translit
from django.test import TestCase
from django.utils.text import slugify

from ..models import Course, Lesson, Exercise
from .factories import CourseFactory, LessonFactory


class CourseTests(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.courses = CourseFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.courses) == self.batch_size

    def test_update(self):
        new_title = 'new title'
        for obj in self.courses:
            obj.title = new_title
            obj.save()
        for obj in self.courses:
            assert obj.title == new_title
            assert re.match(r'^(.+?)\-(.+?)(\-\d+)?$', obj.slug)

    def test_delete(self):
        for obj in self.courses:
            obj.delete()
        courses = Course.objects.all()
        assert not len(courses)

    def test_fields(self):
        for obj in self.courses:
            assert len(obj.title) >= 5
            assert slugify(translit(obj.title, 'ru', reversed=True)) == obj.slug
            assert obj.status == 'draft' or obj.status == 'published'


class LessonTests(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.lessons = LessonFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.lessons) == self.batch_size

    def test_update(self):
        new_title = 'new title'
        new_theory = 'lorem ipsum'
        for obj in self.lessons:
            obj.title = new_title
            obj.theory = new_theory
            obj.save()
        for obj in self.lessons:
            assert obj.title == new_title
            assert obj.theory == new_theory
            assert re.match(r'^(.+?)\-(.+?)(\-\d+)?$', obj.slug)

    def test_delete(self):
        for obj in self.lessons:
            obj.delete()
        lessons = Lesson.objects.all()
        assert not len(lessons)

    def test_fields(self):
        for obj in self.lessons:
            assert len(obj.title) >= 5
            assert len(obj.theory) >= 5
            assert slugify(translit(obj.title, 'ru', reversed=True)) == obj.slug
            assert obj.status == 'draft' or obj.status == 'published'
