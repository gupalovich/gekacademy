import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField


class Course(models.Model):
    """Направление-наука изучения.
       Пример: Математика 1 класс
       url: /<slug>/"""
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
    slug = models.SlugField(default='', max_length=55, unique=True)
    status = StatusField()

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title


class Lesson(TimeStampedModel):
    """Тема урока.
       Пример: Сложение
       url: /<course_slug>/addition/"""
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

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.title


class Exercise(TimeStampedModel):
    """Задача на тематику урока
    url: /<course_slug>/<lesson_slug>/<uuid>"""
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


class ExerciseAnswer(TimeStampedModel):
    """Ответы на задачу"""
    pass


class ExerciseQuestion(TimeStampedModel):
    """Контрольный вопрос"""
    pass
