FROM python:3.13.1-bookworm

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
