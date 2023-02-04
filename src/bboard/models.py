from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=150, verbose_name='Квалификация')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Зарплата')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Специализация')

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Специализации'
        verbose_name = 'Специализация'
        ordering = ['name']
