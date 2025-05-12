# DevOps Microservicio

Este proyecto es parte de un reto técnico. Consiste en un microservicio REST desarrollado en Flask, con seguridad mediante API Key, generación de JWT, pruebas automatizadas, contenerización, balanceador de carga con NGINX y un pipeline CI/CD en GitHub Actions.

## Características principales

- Endpoint POST `/DevOps` protegido por API Key
- Procesamiento de datos JSON (`message`, `to`, `from`, `timeToLifeSec`)
- Generación de token JWT con la información recibida
- Devuelve mensaje personalizado y el token en la respuesta
- Desplegado en dos contenedores balanceados con NGINX
- Pipeline CI/CD con pruebas automáticas (`pytest`) y análisis de estilo (`flake8`)

## Ejecución local

### Construir y ejecutar con Docker Compose

```bash
docker-compose up --build
