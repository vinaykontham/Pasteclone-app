# 📌 Pastebin-like Text Sharing Service (FastAPI)

[![Build Status](https://github.com/your-username/pastebin-app/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/your-username/pastebin-app/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/your-dockerhub-username/pastebin-app.svg)](https://hub.docker.com/r/your-dockerhub-username/pastebin-app)
[![License](https://img.shields.io/github/license/your-username/pastebin-app)](LICENSE)
[![Kubernetes Deployment](https://img.shields.io/badge/Kubernetes-Deployed-brightgreen)](#-kubernetes-deployment-gke)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

---

## 📖 Overview
This project is a **Pastebin-like text snippet sharing service** built with **FastAPI**. Users can create, retrieve, and manage text snippets with **unique links, expiration features, and privacy settings**. 🚀

![image](https://github.com/user-attachments/assets/87eac474-aa5a-4a76-ae3e-49fa454d8ad0)
![image](https://github.com/user-attachments/assets/6e7b9d21-dcb9-4be3-9023-57e06a098345)


---

## ✨ Key Features
- ✅ Generate **unique links** for text snippets  
- ✅ Retrieve, edit, and delete snippets via API  
- ✅ **Expiration mechanism** for temporary pastes  
- ✅ Option to mark pastes as **public or private**  
- ✅ **CI/CD with GitHub Actions** (Testing, Docker Build, GKE Deployment)  
- ✅ **Deployed on Kubernetes (Google Kubernetes Engine - GKE)**  
- ✅ **Database Support**: SQLite (Dev), PostgreSQL (Prod)  

---

## 🛠️ Tech Stack
| Component       | Technology  |
|----------------|------------|
| **Backend**    | FastAPI, Pydantic |
| **Database**   | SQLite (Local) / PostgreSQL (Production) |
| **Cache**      | Redis (Optional) |
| **Container**  | Docker, Docker Compose |
| **Orchestration** | Kubernetes (GKE) |
| **CI/CD**      | GitHub Actions |
| **Testing**    | pytest, Coverage |

---

## 📂 Project Structure
```
├── app/
│   ├── main.py        # FastAPI Application Entry Point
│   ├── config.py      # Database & App Configurations
│   ├── models.py      # SQLAlchemy Models
│   ├── schemas.py     # Pydantic Schemas
│   ├── crud.py        # CRUD Operations
│   ├── routes/        # API Routes
│   ├── templates/     # Jinja2 HTML Templates
│   ├── static/        # CSS, JS Files
├── db/
│   ├── init_db.py     # DB Initialization Script
├── tests/
│   ├── test_routes.py # Unit Tests for API
│   ├── test_utils.py  # Helper Functions Tests
├── k8s/
│   ├── deployment.yaml # Kubernetes Deployment
│   ├── service.yaml    # Kubernetes Service
│   ├── pvc.yaml        # Persistent Volume Claim
├── .github/workflows/
│   ├── ci-cd.yml      # GitHub Actions CI/CD Workflow
├── docker-compose.yml # Local Development Setup
├── Dockerfile         # Container Build File
├── requirements.txt   # Python Dependencies
├── README.md          # Project Documentation
```

---

## 🚀 Installation & Setup
### 🔹 Local Development
1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/vinaykontham/pastebin-app.git  
cd pastebin-app
```

2️⃣ **Create & Activate Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

4️⃣ **Run the Application**  
```sh
uvicorn app.main:app --reload
```
🔗 API will be available at: **http://127.0.0.1:8000**

---

## 🚢 Running with Docker
```sh
docker build -t pastebin-app .
docker run -p 8000:8000 pastebin-app
```

---

## 🧪 Running Tests
```sh
pytest --cov=app tests/
```

---

## 🚀 CI/CD Pipeline (GitHub Actions)
The **GitHub Actions** workflow automates **testing, building, and deploying** the FastAPI app to **Google Kubernetes Engine (GKE)**.

### Workflow Steps
1️⃣ **Run Tests** ✅  
2️⃣ **Build & Push Docker Image** ✅  
3️⃣ **Deploy to GKE** ✅  

### Manually Trigger CI/CD
```sh
git push origin main
```

---

## 🚢 Kubernetes Deployment (GKE)
### 🔹 Prerequisites
- **Google Cloud Project & GKE Cluster**
- **kubectl & gcloud CLI installed**

### 🔹 Deploy to GKE
```sh
kubectl apply -f k8s/
```

### 🔹 Check Deployment
```sh
kubectl get pods
kubectl get services
```

### 🔹 Get External IP
```sh
kubectl get svc pastebin-service
```
🔗 Access App via `EXTERNAL_IP`


---

## 📌 API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| `POST` | `/api/v1/snippets/`    | Create a snippet |
| `GET`  | `/api/v1/snippets/{id}` | Retrieve a snippet |
| `PUT`  | `/api/v1/snippets/{id}` | Edit a snippet |
| `DELETE` | `/api/v1/snippets/{id}` | Delete a snippet |

---

## 📜 License
MIT License © 2025 Your Name

---

### 🎯 Final Thoughts
This **real-world README** provides **structured, professional, and visually appealing** documentation for your **Pastebin-like application**. 🚀  
Let me know if you need **further refinements!** 😊

