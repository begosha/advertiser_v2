# Generated by Django 3.2.6 on 2021-08-21 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='adverts', to='advertiser_app.status', verbose_name='Status'),
        ),
    ]