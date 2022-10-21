import uuid as uuid_lib

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from model_utils import Choices, FieldTracker
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField

from gekacademy.core.utils import get_unique_slug
from .managers import CourseManager, LessonManager


class Course(models.Model):
    """Направление-наука изучения.
       Пример: Математика 1 класс"""
    # manager
    objects = CourseManager()
    # choices
    STATUS = Choices(
        ('draft', _('draft')),
        ('published', _('published')))
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=128, unique=True)
    status = StatusField()
    tracker = FieldTracker(fields=['title'])

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lessons:course', kwargs={'course_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous('title'):
            self.slug = get_unique_slug(Course, self.title)
        return super().save(*args, **kwargs)


class Lesson(TimeStampedModel):
    """Тема урока.
       Пример: Сложение"""
    # manager
    objects = LessonManager()
    # choices
    STATUS = Choices(
        ('draft', _('draft')),
        ('published', _('published')))
    # relations
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        related_query_name='%(class)s',
    )
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=128, unique=True)
    theory = models.TextField(_('Theory'), blank=True, default='')
    experience = models.IntegerField(_('Experience'), default=10)
    premium = models.BooleanField(_('Premium'), default=False)
    status = StatusField()
    tracker = FieldTracker(fields=['title'])

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'lessons:lesson',
            kwargs={'course_slug': self.course.slug, 'lesson_slug': self.slug}
        )

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous('title'):
            self.slug = get_unique_slug(Lesson, self.title)
        return super().save(*args, **kwargs)


class Exercise(TimeStampedModel):
    """Практическая задача на тематику урока"""
    # choices
    DIFFICULTY = [(i, str(i)) for i in range(10)]
    # relations
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        related_query_name='%(class)s',
    )
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    difficulty = models.IntegerField(
        _('Difficulty'),
        choices=DIFFICULTY,
        default=DIFFICULTY[0])
    condition = models.TextField(_('Condition'), default='')
    expression = models.CharField(max_length=255, blank=True, default='')
    answer = models.CharField(max_length=55, default='')
    answers = ArrayField(models.CharField(max_length=55), blank=True, default=list)

    class Meta:
        verbose_name = _('Exercise')
        verbose_name_plural = _('Exercises')

    def get_absolute_url(self):
        return reverse(
            'lessons:exercise',
            kwargs={
                'course_slug': self.lesson.course.slug,
                'lesson_slug': self.lesson.slug,
                'exercise_uuid': self.uuid,
            }
        )

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Achievement(models.Model):
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, default='')
    badge = models.ImageField(
        _('Badge'),
        blank=True,
        default='badges/default.png',
        upload_to='badges/')

    class Meta:
        verbose_name = _('Achievement')
        verbose_name_plural = _('Achievements')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:achievement', kwargs={'uuid', self.uuid})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
