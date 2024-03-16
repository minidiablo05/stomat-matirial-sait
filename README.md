### Как запустить проект:

1)  Клонировать репозиторий и перейти в него в командной строке:
p.s. У меня по какойто причине клонирование через https не работает.
```
git clone https://github.com/minidiablo05/stomat-matirial-sait.git
git clone git@github.com:minidiablo05/stomat-matirial-sait.git
```

```
2)  Преход в командной строке
```
cd stomat-matirial-sait
```

3)  Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

4)  Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

5)  Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

6)  Перейти в папку с кодом
```
cd Sechenov_stomat_progect/
```
7)  Выполнить миграции:

Windows
```
python manage.py makemigrations          p.s. Если здесь выдаёт "No changes detected" пропустите этап, если после проект будет работать, то всё хорошо, иначе напишите мне.
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

8)  Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```