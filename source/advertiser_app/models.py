from django.db import models
from django.contrib.auth import get_user_model
from constants.constants import DEFAULT_STATUS_ID


class Advert(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='adverts',
        verbose_name='Author'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images',
        verbose_name='Image'
    )
    price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Price'
    )
    category = models.ForeignKey(
        'advertiser_app.Category',
        on_delete=models.DO_NOTHING,
        related_name='adverts',
        verbose_name='Category'
    )
    status = models.ForeignKey(
        'advertiser_app.Status',
        default=DEFAULT_STATUS_ID,
        on_delete=models.DO_NOTHING,
        related_name='adverts',
        verbose_name='Status'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    published_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Published At'
    )

    class Meta:
        db_table = 'adverts'
        verbose_name = 'Advert'
        verbose_name_plural = 'Adverts'

    def __str__(self):
        return f'{self.title} - {self.author}'


class Status(models.Model):
    status = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Status'
    )

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.status


class Category(models.Model):
    category = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Category'
    )

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category