import pytest
import logging

from transliterate import translit
from django.test import TestCase
from django.utils.text import slugify

from study.lessons.models import Course
from ..utils import (
    get_unique_slug,
    capitalize_str,
    capitalize_slug,
)


def model_slug_test_generator(cls, test_slug: str, create=5) -> None:
    """"""
    for i in range(create):
        slug = get_unique_slug(cls, test_slug)
        obj = cls.objects.create(title=test_slug, slug=slug)
        res_slug = f'{slugify(test_slug)}-{i}' if i > 0 else slugify(test_slug)
        logging.info(res_slug)
        assert '@' not in res_slug
        assert obj.slug == res_slug


@pytest.mark.django_db
def test_get_unique_slug() -> None:
    """Test unique slug generation; conversion to ru locale"""
    test_slugs = [
        'some @ long giberish-dsfgsdfg!',
        translit('тест @ заголовок!', 'ru', reversed=True),  # test-zagolovok
    ]
    for test_slug in test_slugs:
        model_slug_test_generator(Course, test_slug)


def test_capitalize_str() -> None:
    test_strings = [
        ('test title', 'Test Title'),
        ('test-zagolovok', 'Test-zagolovok'),
        ('тест @ заголовок!', 'Тест @ Заголовок!')]
    for s, result in test_strings:
        func_res = capitalize_str(s)
        assert func_res == result


def test_capitalize_slug() -> None:
    test_slugs = [
        ('test-title', 'Test Title'),
        ('test-zagolovok', 'Test Zagolovok'),
        ('test-zagolovok-1', 'Test Zagolovok'),
    ]
    for s, result in test_slugs:
        func_res = capitalize_slug(s)
        assert func_res == result
