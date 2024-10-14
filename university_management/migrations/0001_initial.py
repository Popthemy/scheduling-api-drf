# Generated by Django 4.2.6 on 2024-10-06 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of your department', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(help_text='The name of the university in full e.g Ladoke Akintola University of Technology', max_length=255, unique=True)),
                ('phone', models.JSONField(help_text='Enter your phone number in a standard json form. A university can have more than one number')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website', models.URLField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name', 'email', 'website'),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_type', models.CharField(choices=[('Bachelor of Science', 'B.Sc'), ('Bachelor of Technology', 'B.Tech'), ('Master of Arts', 'MA'), ('Doctor of Philosophy', 'PhD')], default='Bachelor of Science', max_length=50)),
                ('duration', models.PositiveSmallIntegerField(max_length=10)),
                ('duration_type', models.CharField(choices=[('WEEKLY', 'weekly'), ('MONTHLY', 'monthly'), ('YEARLY', 'yearly')], default='WEEKLY', max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_management.department')),
            ],
            options={
                'ordering': ('degree_type', 'duration'),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of your faculty', max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dean', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_management.institution')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
                'ordering': ('name', 'email'),
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_management.faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='head_of_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
