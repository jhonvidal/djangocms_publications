# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import filer.fields.image
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Post title', max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug (Url of the publication)')),
                ('pub_date', models.DateTimeField(verbose_name='Published on', auto_now_add=True)),
                ('edit_date', models.DateTimeField(verbose_name='Edit on', auto_now=True)),
                ('body', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Post')),
                ('is_publish', models.BooleanField(verbose_name='is publish ?', default=True)),
                ('categories', models.ManyToManyField(verbose_name='Categorias', related_name='post_categories', to='publications.CategoryPost')),
                ('picture', filer.fields.image.FilerImageField(verbose_name='Head picture', to='filer.Image')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag')),
            ],
            options={
                'verbose_name': 'Publication post',
                'verbose_name_plural': 'Publications posts',
            },
        ),
    ]
