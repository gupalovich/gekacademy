import re

from transliterate import translit
from django.test import TestCase
from django.utils.text import slugify

from ..models import Course, Lesson, Exercise, Achievement
from .factories import CourseFactory, LessonFactory, ExerciseFactory, AchievementFactory


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
            assert obj.uuid
            assert len(obj.title) >= 3
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
        courses = Course.objects.all()
        lessons = Lesson.objects.all()
        assert len(courses) == self.batch_size
        assert not len(lessons)

    def test_fields(self):
        for obj in self.lessons:
            assert obj.uuid
            assert obj.course.slug
            assert len(obj.title) >= 3
            assert len(obj.theory) >= 5
            assert obj.experience == 10
            assert slugify(translit(obj.title, 'ru', reversed=True)) == obj.slug
            assert obj.status == 'draft' or obj.status == 'published'


class ExerciseTests(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.exercises = ExerciseFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.exercises) == self.batch_size

    def test_update(self):
        new_difficulty = 11
        for obj in self.exercises:
            obj.difficulty = new_difficulty
            obj.save()
        for obj in self.exercises:
            assert obj.difficulty == new_difficulty

    def test_delete(self):
        for obj in self.exercises:
            obj.delete()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()
        exercises = Exercise.objects.all()
        assert len(courses) == self.batch_size
        assert len(lessons) == self.batch_size
        assert not len(exercises)

    def test_fields(self):
        for obj in self.exercises:
            assert obj.uuid
            assert obj.lesson
            assert obj.lesson.course
            assert isinstance(obj.difficulty, int)
            assert obj.expression
            assert obj.answer
            assert isinstance(obj.answers, list)


class AchievementTests(TestCase):
    def setUp(self):
        self.batch_size = 10
        self.default_badge = 'badges/default.png'
        self.achievements = AchievementFactory.create_batch(size=self.batch_size)

    def test_create(self):
        assert len(self.achievements) == self.batch_size

    def test_update(self):
        new_name = 'new title'
        new_description = 'lorem ipsum'
        for obj in self.achievements:
            obj.name = new_name
            obj.description = new_description
            obj.save()
        for obj in self.achievements:
            assert obj.name == new_name
            assert obj.description == new_description

    def test_delete(self):
        for obj in self.achievements:
            obj.delete()
        achievements = Achievement.objects.all()
        assert not len(achievements)

    def test_fields(self):
        for obj in self.achievements:
            assert obj.uuid
            assert obj.name
            assert obj.description
            assert obj.badge == self.default_badge
