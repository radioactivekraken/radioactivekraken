rm -rf db.sqlite3
rm -rf gamefinder/migrations/0001_initial.py
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
