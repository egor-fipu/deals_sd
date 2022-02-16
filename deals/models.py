from django.db import models


class Deal(models.Model):
    customer = models.CharField('Логин покупателя', max_length=200)
    item = models.CharField('Наименование товара', max_length=200)
    total = models.FloatField('Сумма сделки')
    quantity = models.IntegerField('Количество товара')
    date = models.DateTimeField('Дата и время регистрации сделки')

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-date']

    def __str__(self):
        return f'{self.customer} ({self.date})'


class TopCustomer(models.Model):
    username = models.CharField('Логин клиента', max_length=200)
    spent_money = models.FloatField('Сумма потраченных средств')
    gems = models.JSONField('Список камней')

    class Meta:
        verbose_name = 'Топ'
        verbose_name_plural = 'Топы'
        ordering = ['-spent_money']

    def __str__(self):
        return self.username
