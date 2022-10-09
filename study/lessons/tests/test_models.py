import re

from django.test import TestCase
from django.utils.text import slugify

from ..models import Course, Lesson, Exercise
from .factories import CourseFactory


class CourseTests(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.cources = CourseFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.cources) == self.batch_size

    def test_update(self):
        new_title = 'new title'
        for obj in self.cources:
            obj.title = new_title
            obj.save()
        for obj in self.cources:
            assert obj.title == new_title
            assert re.match(r'^(.+?)\-(.+?)(\-\d+)?$', obj.slug)

    def test_delete(self):
        for obj in self.cources:
            obj.delete()
        courses = Course.objects.all()
        assert not len(courses)

    def test_fields(self):
        for obj in self.cources:
            assert len(obj.title) >= 5
            assert slugify(obj.title) == obj.slug
            assert obj.status == 'draft' or obj.status == 'published'
