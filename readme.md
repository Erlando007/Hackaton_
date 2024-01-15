1. ** Создать и активировать виртуальное окружение **
    ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

2. ** Установите зависимости **
    ```bash
   pip install -r requirements.txt
    ```

3. ** Создайте базу данных **
    ```bash
   psql
   create database 'yourname database'
   ```

4. ** Создайте файл .env и заполните данные **
    ```bash
    Как в env_example
   ```

5. ** Проводите миграции **
    ```bash
    python3 manage.py makemigrations
    python3 migrate
   ```

6. ** Запускаете проект **
    ```bash
    python3 manage.py runserver
   ```

7. ** Запустите celery **
    ```bash
    celery -A your_project_name worker --loglevel=info
    ```

8. ** Зпустите redis **
    ```bash
    redis-server
    ```