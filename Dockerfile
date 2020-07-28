FROM python:3
# workdirectory within the Docker venv
WORKDIR /user/src/app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000
CMD ["python", "./app.py"]





