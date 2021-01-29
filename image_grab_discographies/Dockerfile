FROM python:3.7-buster

WORKDIR /app

COPY fun.py .
COPY grabber.py .
COPY grabber_all.py .
COPY artists.txt .
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt
RUN mkdir trackslist

CMD python grabber_all.py -a artists.txt -f trackslist/tracks.json



