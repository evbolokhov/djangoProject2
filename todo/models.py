from datetime import datetime, timedelta, timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def _get_next_day():

    next_day_datetime = timezone.now() + timedelta(days=1) + timedelta(days=1)
    next_day_datetime.replace(microsecond=0)
    return  next_day_datetime


class TodoTasks(models.Model):
    class StatusChoice(models.IntegerChoices):
        ACTIVE = 1, _("Активно")
        DELAYED = 2, _("Отложено")
        COMPLETE = 3, _("Завершено")

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=False,
                               blank=False,
                               verbose_name="Автор")
    title = models.CharField(max_length=200, null=True, verbose_name="Задача")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    status = models.IntegerField(default=StatusChoice.ACTIVE, choices=StatusChoice.choices, verbose_name="Статус")
    isImportant = models.BooleanField(default=False, verbose_name="Важная")
    isPublic = models.BooleanField(default=False, verbose_name="Публичная")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    resolutionDate = models.DateTimeField(default=_get_next_day, verbose_name="Дата выполнения")

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = _("запись")
        verbose_name_plural = _("записи")

    # @property
    # def authors_str(self):
    #     return ", ".join(str(author) for author in self.author.all())