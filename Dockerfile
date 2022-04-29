FROM tiangolo/uwsgi-nginx:python3.8

WORKDIR /sa-api
ENV UWSGI_INI /sa-api/uwsgi.ini


COPY . /sa-api



RUN pip install -r requirements.txt
