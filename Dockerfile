FROM python:latest

WORKDIR /aiohttp_app

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 80