# Flask Cloud Deployment Project

A production-style Flask web application deployed using Docker and Kubernetes with CI/CD automation.

---

## Features

🚀 Docker containerized application  
☸️ Kubernetes Deployment & Service  
📈 Horizontal Pod Autoscaling (HPA)  
⚙️ Environment configuration using ConfigMap  
🔄 Automated CI/CD pipeline (GitHub Actions)  

---

## Tech Stack

Python (Flask)  
Docker  
Kubernetes (Minikube)  
Git & GitHub Actions  

---

## Project Structure

project1/  
│  
├── app/main.py  
├── Dockerfile  
├── k8s/  
│   ├── deployment.yaml  
│   ├── service.yaml  
│   ├── hpa.yaml  
│   └── configmap.yaml  
└── .github/workflows/ci.yml  

---

## How to Run

### 1️⃣ Build Docker Image
docker build -t riyan999999/project1:latest .

### 2️⃣ Push Image
docker push riyan999999/project1:latest

### 3️⃣ Start Kubernetes
minikube start

### 4️⃣ Deploy Application
kubectl apply -f k8s/

### 5️⃣ Check Status
kubectl get pods  
kubectl get hpa  

---

## Autoscaling

The application scales automatically based on CPU usage.

Minimum replicas: 1  
Maximum replicas: 5  
Target CPU: 50%

---

## Configuration

Application greeting is managed using Kubernetes ConfigMap.

This allows changing environment variables without modifying application code.

---

## Skills Demonstrated

Python development  
Docker containerization  
Kubernetes orchestration  
Horizontal Pod Autoscaling  
ConfigMap usage  
CI/CD automation  
Git version control  

---

## Outcome

End-to-end cloud-native deployment pipeline from development to scalable infrastructure.
