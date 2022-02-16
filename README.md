# deals_sd

## Запуск на локальном сервере

1. Клонировать репозиторий

```bash
git clone https://github.com/egor-fipu/deals_sd.git
```

2. Установить docker и docker-compose

Инструкция по установке доступна в официальной инструкции

3. В папке с проектом создать файл .env

Добавить следующее содержимое
```
SECRET_KEY=secret_django_key
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=deals_db
POSTGRES_USER=user_name
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```
4. В папке с проектом выполнить команду
```
docker-compose up
```

## Описание API

### Загрузка csv-файла
POST-запрос http://127.0.0.1:8000/api/v1/deals/
```
- deals: csv-файл, содержащий историю сделок
```
Ответ
- 200
```
{
    "Status": "OK - файл был обработан без ошибок"
}
```
- 400
```
{
    'Status': 'Error',
    'Desc': <Описание ошибки> - в процессе обработки файла произошла ошибка'
}
```
### Получение результатов обработки файла
GET-запрос http://127.0.0.1:8000/api/v1/deals/

Ответ
- 200
```
{
    "response": [
        {
            "username": "resplendent",
            "spent_money": 451731.0,
            "gems": [
                "Танзанит",
                "Сапфир",
                "Рубин"
            ]
        },
        ...
    ]
}
```