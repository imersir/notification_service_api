## Задача

<p>Необходимо разработать сервис управления рассылками API администрирования и получения статистики.</p>

## Дополнительные задания

<p>Опциональные пункты, выполнение любого количества из приведённого списка повышают ваши шансы на положительное решение о приёме</p>
<ol>
<li>1.организовать тестирование написанного кода</li>
<li>3.подготовить docker-compose для запуска всех сервисов проекта одной командой</li>
<li>5.сделать так, чтобы по адресу /docs/ открывалась страница со drf_yasg UI и в нём отображалось описание разработанного API.</li>
<li>6.реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям</li>
</ol>

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
https://gitlab.com/imersir/notification_service_api
```

### Cоздайте файл .env и заполните переменные окружения:
```
SECRET_KEY=Ключ джанго
ALLOWED_HOSTS=127.0.0.1:8000
DEBUG=Значение (True\False)

API_TOKEN=Ваш токен

DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя базы данных postgres>
POSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль для базы данных>
DB_HOST=db
DB_PORT=5432
```
### Использование на локальном сервере
```
Перейти в раздел notification (cd notification)
Команды миграции
python manage.py makemigrations
python manage.py migrate
```
### Запуск сервера
```
python manage.py runserver
```
### Cоберите docker-compose:
```
Для использования dockera, в файле settings, разкомментировать блок
#PostgreSQL
Для подключения БД PostgreSQL

и удалить блок
#SQlite

Собрать образ и запустить
docker-compose up -d --build
```
### После успешной сборки на сервере выполните команды (только после первого деплоя):
#### Соберите статические файлы:
```
docker-compose exec web python manage.py collectstatic --noinput
```
#### Применитe миграции:
```
docker-compose exec web python manage.py migrate --noinput
```
#### Создать суперпользователя Django:
```
docker-compose exec web python manage.py createsuperuser
```
