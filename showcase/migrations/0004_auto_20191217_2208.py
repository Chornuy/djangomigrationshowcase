# Generated by Django 3.0 on 2019-12-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_auto_20191217_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.TextField(choices=[('review', 'review'), ('published', 'published')], default='review'),
        ),
    ]