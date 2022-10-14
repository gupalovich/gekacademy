from django.db import models


class CourseManager(models.Manager):
    def published(self, **kwargs):
        return self.filter(status='published', **kwargs)


class LessonManager(models.Manager):
    def published(self, **kwargs):
        return self.filter(status='published', **kwargs)
