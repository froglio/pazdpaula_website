# Generated by Django 3.1.5 on 2021-04-30 13:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0012_remove_post_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
