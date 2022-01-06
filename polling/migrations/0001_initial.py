# Ioana A Mititean
# UWPCE Course 3 - Internet Programming in Python
# Django

"""
Initial migration file, generated by Django. Includes a Migration class that creates the Poll
model.
"""

# Generated by Django 4.0 on 2021-12-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    """
    Migration class - specifies the operation to create the Poll model.
    """

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
