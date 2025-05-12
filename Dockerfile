# Usamos una imagen base de Python
FROM python:3.9-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el código actual al contenedor
COPY . .

# Instalamos las dependencias necesarias
RUN pip install flask pyjwt

# Expone el puerto 5000 para que pueda ser accedido desde fuera
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "microservicio.py"]