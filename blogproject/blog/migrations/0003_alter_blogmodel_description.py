# Generated by Django 4.2.3 on 2023-08-01 16:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogmodel_category_blogmodel_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
