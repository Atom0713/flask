FROM python:3.6-alpine

WORKDIR /flaskapp
COPY . /flaskapp


#RUN apk add --no-cache mariadb-dev build-base
RUN python -m pip install --upgrade pip && pip install --no-cache -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]




