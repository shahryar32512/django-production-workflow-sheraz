# Python 3.10 lightweight base image
FROM python:3.10-slim

# Container ke andar working directory
WORKDIR /app

# Python dependencies install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project ki files container mein copy karna
COPY . .

# Django application ka port
EXPOSE 8000

# Django development server start karna
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
