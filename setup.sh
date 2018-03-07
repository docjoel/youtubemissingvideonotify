apk update
apk add py3-psycopg2
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations YT_models
python3 manage.py migrate
python3 manage.py test channel_models
