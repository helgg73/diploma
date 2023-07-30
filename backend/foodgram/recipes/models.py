from django.db import models


class Tags(models.Model):
    '''Класс Tags используется для описания тэгов
    кулинарных рецептов
    '''
    name = models.CharField(
        'Название тэга',
        help_text='Введите название тэга',
        max_length=200,
        unique=True,
    )
    color = models.CharField(
        'Цвет тэга',
        help_text='Введите код цвета тэга',
        max_length=7,
        null=True,
        unique=True,
    )
    slug = models.SlugField(
        'Слаг тэга',
        help_text='Введите слаг тэга',
        max_length=200,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self) -> str:
        return self.name
