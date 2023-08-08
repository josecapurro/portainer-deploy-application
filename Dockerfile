FROM python:3.9
EXPOSE 9999/tcp
WORKDIR ./app
COPY cantakerousmarket /app
COPY requirements.txt /app
RUN ["pip3", "install", "-r", "requirements.txt", "--no-cache-dir"]
RUN [ "python3", "manage.py", "migrate" ]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:9999", "--settings=cantakerousmarket.settings" ]
