FROM python:3.8

COPY requirements.txt .

# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV && 
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

# Simplifies the path issue.
RUN pip3 install gunicorn

COPY app.py .
COPY shitlog.log .

ADD . /code
WORKDIR /code
COPY . .