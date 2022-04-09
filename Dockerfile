FROM python:3.8-slim-buster
RUN apt-get update
WORKDIR /scoringservice
COPY . /scoringservice
RUN pip install -r requirements.txt
EXPOSE 8081
CMD [ "python", "./main.py" ]