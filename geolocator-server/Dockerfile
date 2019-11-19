FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install flask
RUN pip install psycopg2
RUN pip install requests
COPY server.py /usr/bin/local/
EXPOSE 5000
ENTRYPOINT ["python3", "/usr/bin/local/server.py"]
