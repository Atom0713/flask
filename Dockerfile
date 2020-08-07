FROM python:3.6-alpine

WORKDIR /flaskapp
COPY . /flaskapp
#RUN apk add --no-cache mariadb-dev build-base
RUN python -m pip install --upgrade pip && pip install --no-cache -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]

FROM mysql:8.0.2
ENV MYSQL_ROOT_PASSWORD: 123
ENV MYSQL_DATABASE: returns_test
ENV MYSQL_USER: yayloh
ENV MYSQL_PASSWORD: admin
ADD ./scripts/setup.sql /docker-entrypoint-initdb.d
EXPOSE 3306




