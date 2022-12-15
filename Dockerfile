FROM python:3.8


WORKDIR /code

COPY . .

COPY app.py .

RUN pip install -r requirements.txt

RUN pip3 install gunicorn

ENV FLASK_APP app.py 