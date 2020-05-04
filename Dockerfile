FROM python:3.7.3-stretch

RUN mkdir /code/
WORKDIR /code/

ADD requirements.txt /requirements.txt
RUN python -m pip install -r /requirements.txt

ADD . /code/

ENV CLIENT_TOKEN=${CLIENT_TOKEN}
ENV API_TOKEN=${API_TOKEN}

CMD ["python", "bot.py"]
