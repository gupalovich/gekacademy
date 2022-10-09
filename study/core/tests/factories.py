from django.utils.text import slugify

from ..utils import get_unique_slug


def model_slug_test_generator(cls, test_slug: str, create=5) -> None:
    for i in range(create):
        slug = get_unique_slug(cls, test_slug)
        obj = cls.objects.create(title=test_slug, slug=slug)
        res_slug = f'{slugify(test_slug)}-{i}' if i > 0 else slugify(test_slug)
        assert '@' not in res_slug
        assert obj.slug == res_slug
