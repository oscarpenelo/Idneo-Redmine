#  docker run --name idneoredmine -p 80:80 -i -t idneoredmine python redmine.py

FROM python:2.7
WORKDIR /opt/app
COPY . /opt/app
COPY requirements.txt /tmp/
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --requirement /tmp/requirements.txt
