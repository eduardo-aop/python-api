# set base image (host OS)
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 5432
EXPOSE 5000
# command to run on container start
CMD [ "python", "main.py" ]