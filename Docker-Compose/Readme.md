**Overview**

A microservices-based To-Do List Application built using:

Spring Boot (Java) for the backend REST API

Flask (Python) for the frontend user interface

Docker Compose to orchestrate both containers seamlessly

This project demonstrates container networking, RESTful service communication, and full-stack development inside Docker

**Tech Stack** 

| Layer             | Technology         | Description                                     |
| ----------------- | ------------------ | ----------------------------------------------- |
| **Frontend**      | Flask + Bootstrap  | HTML UI to add & delete tasks                   |
| **Backend**       | Spring Boot (Java) | REST API with endpoints `/tasks`, `/tasks/{id}` |
| **Orchestration** | Docker Compose     | Runs both apps on the same network              |
| **Build Tools**   | Maven + Pip        | Backend & frontend dependencies                 |

## 🐳 **How to Run Locally**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/rutuja-jadhav29/MLOps-Labs.git
cd MLOps-Labs/Docker-Compose '''



----

2️⃣ Build and Run the Containers
docker compose up --build



