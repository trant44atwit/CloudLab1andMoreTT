FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9600

CMD ["uvicorn", "loadbalancer:app", "--host", "0.0.0.0", "--port", "9600"]
