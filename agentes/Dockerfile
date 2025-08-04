# Etapa base
FROM python:3.13-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia primero los archivos necesarios para instalar dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir uvicorn

# Copia el resto del proyecto
COPY . .

# Expone el puerto de la app
EXPOSE 8080

# Comando por defecto para correr FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
