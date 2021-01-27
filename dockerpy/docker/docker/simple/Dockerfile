FROM python:3.7-buster

WORKDIR /app

COPY input.json
COPY fun.py .
COPY app.py .
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD ["python","app.py","-f","intput.json","-s","output.json"]

