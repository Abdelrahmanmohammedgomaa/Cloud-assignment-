#Dockerfile
FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY cloud.py .
copy paragraphs.txt .
cmd ["python","script.py"]