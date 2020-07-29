FROM python:3.6-alpine

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]



