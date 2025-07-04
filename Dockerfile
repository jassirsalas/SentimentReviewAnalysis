FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y && \
    pip install --no-cache-dir -r requirements.txt
    
COPY . .

RUN python main.py

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]