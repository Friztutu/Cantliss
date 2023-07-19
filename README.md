<p align="center">
      <img src="https://i.ibb.co/0fkHMJV/pngegg.png" width="420">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/python-3.10-green" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-3.2.18-yellowgreen" alt="Parser Version">
   <img src="https://img.shields.io/badge/Licence-MIT-blueviolet" alt="License">
</p>

## О проекте

Реализация frontend(Html and CSS) и backend(Django) интернет магазина. Реализована пагинация, фильтрация по категориям и подкатегориям, поиск по названию товара, корзина, избранные товары, 
возможность оформить заказ с помощью yookassa(тестовый платеж, с использованием тестовых карт, без реальных денег), список заказов с их статусами(Создан, оплачен, в пути, доставлен), отдельная админ панель сотрудников
для измения статусов заказов. Сайт адаптирован под пк, планшеты и мобильные устройства разных размеров.

Проект деплойнут, оценить его можно по ссылке - https://cantliss.ru/

## Превью
<b>Главная страница:</b>

<img src="https://i.ibb.co/dghCPYs/2023-07-19-200438.png" width="100%">

<b>Каталог:</b>

<img src="https://i.ibb.co/h1VkbLz/2023-07-19-200005.png" width="100%">

<b>Профиль:</b>

<img src="https://i.ibb.co/3pMT7vM/2023-07-19-200106.png"  width="100%">

## Настройка окружения для работы
1. Сначала нужно создать и запустить виртуальное окружение:
 ```bash
   python3.10 -m venv venv
   source venv/bin/activate
 ```
2. Скачать пакеты:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
3. Создать и заполнить файл .env в корневой папке проета:<br><br>
Получить новый secret key можно так:
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
4. Провести миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Загрузить fixtures:
```bash
python manage.py loaddata products.ProductGender
python manage.py loaddata products.ProductCategory
python manage.py loaddata products.TypeProduct
python manage.py loaddata products.Product
```

# Запуск на локалке
```bash
python manage.py runserver
```


## Разработчик:

- [Alex](https://github.com/Friztutu)

## License

Project Store is distributed under the MIT licence
