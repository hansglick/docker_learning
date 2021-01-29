FROM python:3.7-buster

ENV FIRSTNAME=james
ENV LASTNAME=ruskin
ENV outputfile output.json

WORKDIR /app

COPY fun.py .
COPY grabber.py .
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD python grabber.py -a $FIRSTNAME $LASTNAME -f output.json