FROM python:3
# workdirectory within the Docker venv
WORKDIR /user/src/app

COPY app.py .
COPY requirements.txt .
COPY start.sh .

RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["./start.sh"]





