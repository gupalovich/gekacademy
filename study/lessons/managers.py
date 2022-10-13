from django.db import models


class CourseQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')


class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class LessonQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')


class LessonManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()
