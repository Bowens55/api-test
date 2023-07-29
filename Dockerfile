FROM python:slim 

RUN apt-get update \ 
    && apt-get upgrade 

WORKDIR /api

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./*.py /api/

CMD [ "uvicorn","main:app","--reload"]
