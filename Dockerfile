FROM python:slim 

RUN apt-get update -y \ 
    && apt-get upgrade -y  
    # && apt-get install -y python3-pip

WORKDIR /api

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./*.py /api/

CMD [ "uvicorn","main:app","--reload"]
