# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-06 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160805_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='mentorship',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentees', to='app.Member'),
        ),
        migrations.AddField(
            model_name='mentorship',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='app.Member'),
        ),
        migrations.AddField(
            model_name='mentorship',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Skill'),
        ),
        migrations.AddField(
            model_name='member',
            name='mentorship',
            field=models.ManyToManyField(related_name='_member_mentorship_+', through='app.Mentorship', to='app.Member'),
        ),
    ]