# 🐟 Masterpiece Farm Produce - Catfish Shop

A Flask web application for selling catfish products, deployed on Kubernetes using Helm.

## Tech Stack
- Python / Flask
- Docker
- Kubernetes (minikube)
- Helm
- Prometheus + Grafana (monitoring)
- SonarQube (code quality)

## Run Locally
```bash
python app.py
```

## Deploy with Docker
```bash
docker build -t catfish-app-v2:latest .
docker run -p 80:80 catfish-app-v2
```

## Deploy with Helm on Minikube
```bash
eval $(minikube docker-env)
docker build -t catfish-app-v2:latest .
helm install catfish-shop ~/catfish-helm
minikube service catfish-shop-service --url
```

## Routes
- `/` - Home
- `/inventory` - View all catfish products
- `/health` - Health check endpoint
