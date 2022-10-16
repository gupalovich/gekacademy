import uuid as uuid_lib

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Promotion(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, default='')
    discount = models.FloatField(_('Discount'), default=0.0)

    class Meta:
        verbose_name = _('Promotion')
        verbose_name_plural = _('Promotions')

    def __str__(self):
        return '%s-%.2f' % (self.name, self.discount)


class Product(TimeStampedModel):
    # choices
    class Currency(models.TextChoices):
        RUB = '₽', _('Ruble')
        DOLLAR = '$', _('Dollar')
        EURO = '€', _('Euro')
    # relations
    promotion = models.ManyToManyField(Promotion, related_name='%(class)ss', blank=True)
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, default='')
    price = models.FloatField(_('Price'), default=0.0)
    currency = models.CharField(max_length=2, choices=Currency.choices, default=Currency.RUB)
    image = models.ImageField(_('Poster'), blank=True, default='', upload_to='products/')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    class Status(models.TextChoices):
        FAILED = 'FAILED', _('Failed')
        PENDING = 'PENDING', _('Pending')
        SUCCESS = 'SUCCESS', _('Success')
    # relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # fields
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=55, choices=Status.choices, default=Status.PENDING)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.uuid
