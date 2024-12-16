FROM python:3.11.11-alpine
WORKDIR /app
COPY . /app
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","main.py"]
