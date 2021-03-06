# Generated by Django 3.0 on 2019-12-17 22:08

from django.db import migrations, models
import uuid


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# showcase.migrations.0003_auto_20191217_2203

def set_all_created_model_as_published(aps):
    PostCls = aps.get_model('showcase', 'Post')
    PostCls.objects.update(status=PostCls.PUBLISHED)


class Migration(migrations.Migration):

    replaces = [('showcase', '0001_initial'), ('showcase', '0002_post_status'), ('showcase', '0003_auto_20191217_2203'), ('showcase', '0004_auto_20191217_2208')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('status', models.TextField(choices=[('review', 'review'), ('published', 'published')], default='published')),
            ],
        ),
        migrations.RunPython(
            code=set_all_created_model_as_published,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.TextField(choices=[('review', 'review'), ('published', 'published')], default='review'),
        ),
    ]
