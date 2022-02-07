FROM python:3.9-bullseye
RUN apt-get update && apt-get upgrade 
RUN pip install psycopg2
COPY ./webdb.py . 
CMD python3 webdb.py
