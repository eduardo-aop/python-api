# set base image (host OS)
FROM python:3.9


RUN python -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR app

COPY ./app /

EXPOSE 5000
# command to run on container start
CMD [ "python", "-u", "-B", "main.py" ]