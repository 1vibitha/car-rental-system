# Generated by Django 5.1 on 2024-09-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
