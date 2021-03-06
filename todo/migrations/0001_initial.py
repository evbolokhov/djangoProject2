# Generated by Django 4.0.4 on 2022-05-30 18:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Задача')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.IntegerField(choices=[(1, 'Активно'), (2, 'Отложено'), (3, 'Завершено')], default=1, verbose_name='Статус')),
                ('isImportant', models.BooleanField(default=False, verbose_name='Важная')),
                ('isPublic', models.BooleanField(default=False, verbose_name='Публичная')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('resolutionDate', models.DateTimeField(default=datetime.datetime(2022, 5, 31, 21, 52, 18, 688362), verbose_name='Дата выполнения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
