# Generated by Django 5.1 on 2024-09-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_image_category_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='images',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]
