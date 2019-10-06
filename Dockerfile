FROM python:3.7-alpine
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app.py /app
COPY jokes /app/jokes
COPY templates app/templates
CMD python3 /app/app.py
