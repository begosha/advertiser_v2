# Generated by Django 3.2.6 on 2021-08-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_app', '0004_auto_20210821_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published At'),
        ),
    ]