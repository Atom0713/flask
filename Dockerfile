FROM python:2
# workdirectory within the Docker venv
WORKDIR /user/src/app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./app.py"]





