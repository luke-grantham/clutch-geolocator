FROM python:3.8-alpine
RUN pip install requests
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
COPY server.py /usr/bin/local/
EXPOSE 9900
CMD python3 /usr/bin/local/server.py

