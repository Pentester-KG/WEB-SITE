# Generated by Django 5.0.4 on 2024-05-28 04:55

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.PositiveSmallIntegerField(default=18, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(60)])),
                ('phone_number', models.CharField(default='+996', max_length=14)),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=64)),
                ('exp_work', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)])),
                ('experience_work', models.CharField(default='Стаж не определен', max_length=100)),
                ('married_status', models.CharField(choices=[('Женат(а)', 'Женат(а)'), ('Не женат(а)', 'Не женат(а)')], default='Не женат/Не замужем', max_length=100)),
                ('education', models.BooleanField(default=False)),
                ('habits', models.CharField(default=None, max_length=200)),
                ('email1', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
