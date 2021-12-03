FROM python:3.7

RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
&& apt-get -y install apt-utils gcc libpq-dev libsndfile-dev 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]