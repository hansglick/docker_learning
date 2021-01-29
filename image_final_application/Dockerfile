FROM python:3.7-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN apt-get -y -qq update && \
	apt-get install -y -qq curl && \	
	apt-get clean
RUN curl -o /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq && chmod +x /usr/local/bin/jq

WORKDIR /app
RUN mkdir trackslist
RUN mkdir songs

COPY fun.py .
COPY grabber.py .
COPY grabber_all.py .
COPY artists.txt .
COPY run.sh .
COPY assembler.py .
COPY grabber_youtube_links.py .
COPY requirements.txt /tmp
COPY dwlsongs.sh /app/songs
COPY dwl_comments.py .

RUN pip install -r /tmp/requirements.txt

CMD sh run.sh artists.txt
