import uuid as uuid_lib

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from model_utils import Choices, FieldTracker
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField

from study.core.utils import get_unique_slug


class Course(models.Model):
    """Направление-наука изучения.
       Пример: Математика 1 класс"""
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
    slug = models.SlugField(default='', max_length=255, unique=True)
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
    # choices
    STATUS = Choices(
        ('draft', _('draft')),
        ('published', _('published')))
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        related_query_name='%(class)s',
    )
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)
    theory = models.TextField(_('Theory'), blank=True, default='')
    status = StatusField()
    tracker = FieldTracker(fields=['title'])

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lessons:lesson', kwargs={'lesson_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.tracker.previous('title'):
            self.slug = get_unique_slug(Lesson, self.title)
        return super().save(*args, **kwargs)


class Exercise(TimeStampedModel):
    """Практическая задача на тематику урока"""
    # choices
    DIFFICULTY = [(i, str(i)) for i in range(10)]
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        related_query_name='%(class)s',
    )
    difficulty = models.IntegerField(
        _('Difficulty'),
        choices=DIFFICULTY,
        default=DIFFICULTY[0])

    class Meta:
        verbose_name = _('Exercise')
        verbose_name_plural = _('Exercises')

    def get_absolute_url(self):
        return reverse('lessons:exercise', kwargs={'exercise_uuid': self.uuid})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class ExerciseAnswer(TimeStampedModel):
    """Ответы на задачу"""
    pass


class ExerciseQuestion(TimeStampedModel):
    """Контрольный вопрос"""
    pass
