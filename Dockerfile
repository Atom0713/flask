FROM python:3.6-alpine

WORKDIR /flaskapp
COPY . /flaskapp

#RUN apk update \
#    && apk add --virtual build-deps gcc python3-dev musl-dev \
#    &&  apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev \
#    && apk add --no-cache mariadb-dev
#RUN pip3 install PyMySQL
RUN python -m pip install --upgrade pip && pip install --no-cache -r requirements.txt
RUN pip install pytest pytest-cov
#RUN apk del build-deps

ENTRYPOINT ["python"]
CMD ["test.py"]




