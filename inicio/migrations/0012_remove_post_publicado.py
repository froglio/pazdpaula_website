# Generated by Django 3.1.5 on 2021-04-16 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0011_post_criado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publicado',
        ),
    ]
