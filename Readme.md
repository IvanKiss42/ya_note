:grey_exclamation: Это проект блога, в котором я отрабатывал навыки работы с Unittest в Django проектах: тесты проверяют CRUD запросы и отображение основных страница проекта в зависимости от прав пользователя.

YaNote - проект простого сайта-записной книжки, основной особенностью которого - возможность для пользователя просмотра только собственных записей.

:computer: Стек технологий: Python, Django, Unittest, SQLite

:electric_plug: Проект предназначен для локального использования.  
После клонирования репозитория, в корневой папке проекта установите виртуальное окружение:  
python -m venv venv  
Активируйте виртуальное окружение:  
source venv/Scripts/activate  

Установите зависимости из файла requirements.txt:  
python -m pip install --upgrade pip  
pip install -r requirements.txt  

Для запуска тестов из корневой папки проекта воспользуйтесь командой:  
python manage.py test  

Примените миграции и запустите локальный сервер:  
python manage.py migrate  
python manage.py runserver  
  
Проект будет доступен по локальному адресу: http://127.0.0.1:8000/  