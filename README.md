# 🗳️ Multi-Container Voting App

A Docker-based multi-container voting application that demonstrates microservices architecture using Docker Compose. Users can vote between two options, and the results are processed and displayed in real time.

## 📌 Project Overview

This project consists of multiple services running in separate Docker containers that work together to provide a complete voting system.

### Architecture

```
+-------------+
|   Vote App  |
+-------------+
       |
       v
+-------------+
|    Redis    |
+-------------+
       |
       v
+-------------+
|   Worker    |
+-------------+
       |
       v
+-------------+
| PostgreSQL  |
+-------------+
       |
       v
+-------------+
| Result App  |
+-------------+
```

## 🚀 Features

- Multi-container application using Docker Compose
- Real-time vote processing
- Redis message queue
- PostgreSQL database
- Container networking
- Microservices architecture
- Easy deployment and scalability

---

## 🛠️ Technologies Used

- Docker
- Docker Compose
- Redis
- PostgreSQL
- Python
- Node.js
- HTML/CSS
- Microservices Architecture

---

## 📂 Project Structure

```bash
Multi-Container-Voting-app/
│
├── vote/
│   ├── Dockerfile
│   └── source code
│
├── result/
│   ├── Dockerfile
│   └── source code
│
├── worker/
│   ├── Dockerfile
│   └── source code
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Prerequisites

Before running this project, ensure that the following are installed:

- Docker
- Docker Compose

Verify installation:

```bash
docker --version
docker compose version
```

---

## 📥 Clone Repository

```bash
git clone https://github.com/Hetpatel7051/Multi-Container-Voting-app.git
cd Multi-Container-Voting-app
```

---

## ▶️ Run the Application

Build and start all services:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

---

## 🌐 Access the Application

After the containers start successfully:

### Voting Application

```text
http://localhost:5000
```

### Results Application

```text
http://localhost:5001
```

> Note: Ports may differ depending on your docker-compose configuration.

---

## 🐳 Docker Commands

### View Running Containers

```bash
docker ps
```

### View Logs

```bash
docker compose logs -f
```

### Stop Containers

```bash
docker compose down
```

### Stop and Remove Volumes

```bash
docker compose down -v
```

---

## 🔄 Application Workflow

1. User submits a vote through the Vote App.
2. Vote data is sent to Redis.
3. Worker service processes the vote.
4. Processed vote is stored in PostgreSQL.
5. Result App fetches data from PostgreSQL.
6. Live voting results are displayed to users.

---

## 📚 Learning Outcomes

This project helps understand:

- Docker Fundamentals
- Docker Compose
- Container Networking
- Redis Integration
- PostgreSQL Integration
- Microservices Communication
- Multi-Container Deployments
- DevOps Concepts

---

## 📸 Screenshots

### Voting Page

Add screenshot here:

```text
screenshots/vote-page.png
```

### Result Page

Add screenshot here:

```text
screenshots/result-page.png
```

---

## 🤝 Contributing

Contributions are welcome.

### Steps

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Het Patel**

GitHub: https://github.com/Hetpatel7051

Repository: https://github.com/Hetpatel7051/Multi-Container-Voting-app

---

⭐ If you found this project useful, don't forget to star the repository.