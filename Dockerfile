# Usa una imagen base de Python oficial, optimizada y liviana
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto al contenedor
COPY . .

# Expone el puerto por si la aplicación lo necesitara (aunque este bot no lo usa, es buena práctica)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "src/main.py"]