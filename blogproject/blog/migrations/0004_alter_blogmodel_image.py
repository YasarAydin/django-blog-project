# Generated by Django 4.2.3 on 2023-08-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
