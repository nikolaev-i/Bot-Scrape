FROM python:3.11-alpine3.19

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

