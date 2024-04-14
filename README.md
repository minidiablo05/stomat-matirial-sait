### Как запустить проект:

1)  Выберите папку где хотите сохранить код сайта и перейдите в неё в командной строке.

2)  Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/minidiablo05/stomat-matirial-sait.git
или
git clone git@github.com:minidiablo05/stomat-matirial-sait.git
```

3)  Преход в командной строке

```
cd stomat-matirial-sait
```

4)  Cоздать виртуальное окружение:

Windows
```
python -m venv venv
```
Linux/macOS
```
python3 -m venv venv
```

5)  Aктивировать виртуальное окружение:

Windows
```
Если работаете в Git Bash:  source venv/Scripts/activate
Если работаете в PowerShell:  venv\Scripts\activate
Если работаете в командной строке (cmd):  venv\Scripts\activate
```
Linux/macOS
```
source venv/bin/activate
```

6)  Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

7)  Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

8)  Перейти в папку с кодом

```
cd Sechenov_stomat_progect/
```

9)  Выполнить миграции 1:

p.s. Если здесь выдаёт "No changes detected" пропустите этап, если после проект будет работать, то всё хорошо, иначе напишите мне.

Windows
```
python manage.py makemigrations          
```

Linux/macOS
```
python3 manage.py migrate
```

10)  Выполнить миграции 2:

Windows
```          
python manage.py migrate                 
```

Linux/macOS
```
python3 manage.py makemigrations
```

11)  Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```

После этого по адресу http://127.0.0.1:8000/ в адресной строке будет доступен сайт.


### Обновить материалы сайта.

В консоль введите (git pull)