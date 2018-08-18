# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-15 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('identifier', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'MyUser',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('create_date', models.DateField(auto_now=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('context', models.TextField()),
                ('is_show', models.BooleanField()),
            ],
            options={
                'db_table': 'ariticle',
            },
        ),
    ]
