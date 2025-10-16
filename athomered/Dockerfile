
FROM python:3.11-slim

# Dependencias de compilación (argon2/bcrypt)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Primero requirements para cacheo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Luego el código
COPY . .

EXPOSE 8000

# Por defecto (puede ser overrideado por docker-compose)
CMD [ "uvicorn", "app.principal:app", "--host", "0.0.0.0", "--port", "8000" ]
