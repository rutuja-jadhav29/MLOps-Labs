### **Overview**

A microservices-based To-Do List Application built using:

- Spring Boot (Java) for the backend REST API

- Flask (Python) for the frontend user interface

- Docker Compose to orchestrate both containers seamlessly

This project demonstrates container networking, RESTful service communication, and full-stack development inside Docker

### **Tech Stack** 

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
cd MLOps-Labs/Docker-Compose
```

### **2️⃣ Build and Run the Containers**
```bash
docker compose up --build
```

This command

- Builds both backend (Spring Boot) and frontend (Flask) images

- Starts the containers

- Connects them over Docker’s internal network

### **3️⃣ Access the Application**
| Service                   | URL                                                        | Description            |
| ------------------------- | ---------------------------------------------------------- | ---------------------- |
| **Frontend (Flask)**      | [http://localhost:45000](http://localhost:45000)           | Web UI for tasks       |
| **Backend (Spring Boot)** | [http://localhost:8080/tasks](http://localhost:8080/tasks) | REST API JSON endpoint |

<img width="756" height="563" alt="Screenshot 2025-10-20 at 9 48 33 PM" src="https://github.com/user-attachments/assets/921fb4fa-86a4-4177-ae70-29c3f72c3468" />

Add into the list

<img width="803" height="450" alt="Screenshot 2025-10-20 at 9 48 42 PM" src="https://github.com/user-attachments/assets/ee7e6216-3919-4ea4-8aa4-bd3c73d2d7cb" />


Delete the Second to-do point

### **Features**
✅ Add new tasks
✅ Delete existing tasks
✅ Automatic network communication between Flask ↔ Spring Boot
✅ Live API interaction via REST
✅ Fully containerized and reproducible setup

### **Project Structure**

```bash
Docker-Compose/
│
├── docker-compose.yml        # Orchestrates both services
│
├── todo-backend/             # Spring Boot Backend
│   ├── src/main/java/...     # Java source files
│   ├── pom.xml               # Maven config
│   └── Dockerfile            # Backend container image
│
└── todo-frontend/            # Flask Frontend
    ├── app.py                # Main Flask app
    ├── templates/index.html  # HTML UI
    ├── requirements.txt      # Python dependencies
    └── Dockerfile            # Frontend container image

```

### **How It Works**

Flask (Frontend) sends HTTP requests to the backend service name (spring-boot-app) over port 8080.

Spring Boot (Backend) processes requests and maintains an in-memory task list.

Docker Compose provides service discovery and internal networking.
