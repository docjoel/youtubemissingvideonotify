apk update
apk add libpq-dev python3-dev
apk add postgresql-server-dev-all
apk add py3-psycopg2
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations channel_models
python3 manage.py migrate
python3 manage.py test channel_models
