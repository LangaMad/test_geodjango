Проект на основе GeoDjango с использованием PostGIS для работы с географическими данными.

Требования:
Python 3.10+
PostgreSQL 15+ с PostGIS
GDAL, GEOS, PROJ для работы с географическими данными(https://trac.osgeo.org/osgeo4w/)
Django 4+
Django REST Framework
Django REST Framework GIS


Установка Шаг 1: Клонировать репозиторий Клонируйте репозиторий на ваше устройство:

git clone git@github.com:LangaMad/test_geodjango.git (SSH)
https://github.com/LangaMad/test_geodjango.git (HTTP)

Установка:
 Создайте и активируйте виртуальное окружение
python -m venv venv
venv\Scripts\activate  # для Windows
 Установите зависимости
pip install -r requirements.txt


Шаг 2: Скопировать файл переменных окружения Создайте файл .env в корневой папке проекта (geodjango). Этот файл будет использоваться для хранения чувствительных данных, таких как настройки базы данных.

SECRET_KEY='your-django-secret-key'
DEBUG=True

GDAL_LIBRARY_PATH=C:/OSGeo4W/bin/gdal310.dll
OSGEO4W_ROOT=C:\OSGeo4W
GDAL_DATA=C:\OSGeo4W\apps\gdal\share\gdal
PROJ_LIB=C:\OSGeo4W\share\proj
PATH=C:\OSGeo4W\bin

# Настройки базы данных
DB_NAME=db
DB_USER=user
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=5432
Замените значения на нужные (если необходимо).

Создайте базу данных в PostgreSQL:
Подключитесь к базе данных и выполните команду:
CREATE EXTENSION postgis;

Шаг 3: Запуск проекта
Примените миграции для создания таблиц в базе данных:
python manage.py migrate

Создайте суперпользователя для доступа к админке:
python manage.py createsuperuser

Запустите сервер:
python manage.py runserver

Теперь проект доступен по адресу:
http://127.0.0.1:8000/

Шаг4: Тестирование API
Войти в Django Admin по адресу http://127.0.0.1:8000/admin/ с учетными данными суперпользователя.

Добавление нового места (в формате координат):
{
  "name": "My Place",
  "location": [30.5234, 50.4501]
}
Метод: POST, эндпоинт: /api/places/

Получить список мест:
Метод: GET, эндпоинт: /api/places/


