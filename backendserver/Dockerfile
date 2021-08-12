FROM python:3
WORKDIR /usr/src/app
EXPOSE 8000
COPY server.py /usr/src/app/
COPY consume.py /usr/src/app/
CMD [ "python", "server.py" ]