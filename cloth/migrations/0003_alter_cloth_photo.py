# Generated by Django 5.0.4 on 2024-05-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0002_cloth_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/clothes'),
        ),
    ]
