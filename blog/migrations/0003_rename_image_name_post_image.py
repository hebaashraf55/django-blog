# Generated by Django 4.1.6 on 2023-02-24 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_name',
            new_name='image',
        ),
    ]
