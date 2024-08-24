@echo off

:: Create a virtual environment and activate it
py -3.12 -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r test_task_2/requirements.txt

:: Make the migrations
python manage.py makemigrations

:: Apply migrations
python manage.py migrate

:: Create a superuser
echo Creating superuser...
python manage.py createsuperuser

:: Run the server
python manage.py runserver

:: Pause the script to allow the user to see the output
pause