# Deploying a Streamlit App with PostgreSQL in Docker

## 📌 Overview
This project demonstrates how to deploy a **Streamlit application** that connects to a **PostgreSQL database** using Docker. The application fetches and displays passenger data stored in PostgreSQL, ensuring a seamless and containerized workflow.

## 📁 Project Structure
```
Streamlit-Postgres-Docker/
│── Dockerfile
│── main.py
```

### 🔹 Description of Files:
- **main.py** – Streamlit app that connects to PostgreSQL and fetches data.
- **Dockerfile** – Configuration for containerizing the Streamlit app.

## 🛠 Setting Up PostgreSQL in Docker

### **1️⃣ Pull the PostgreSQL Docker Image**
```bash
docker pull postgres:latest
```

### **2️⃣ Create a Docker Network**
```bash
docker network create my_postgres_network
```

### **3️⃣ Run the PostgreSQL Container**
```bash
docker run --name my_postgres_container --network my_postgres_network \
-e POSTGRES_USER=aaradhya -e POSTGRES_PASSWORD=secret \
-e POSTGRES_DB=testdb -p 5432:5432 -d postgres
```

## 💾 Creating and Populating the Database
### **4️⃣ Access PostgreSQL**
```bash
docker exec -it my_postgres_container psql -U aaradhya -d testdb
```

### **5️⃣ Create the `passengers` Table**
```sql
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);
```

### **6️⃣ Insert Sample Data**
```sql
INSERT INTO passengers (name, location) VALUES
('Aaradhya', 'Dehradun'),
('Aryan', 'Jind'),
('Aaru', 'Pathankot');
```
Exit the shell using:
```bash
\q
```

## 🎨 Streamlit Application Setup
### **7️⃣ Create a `main.py` File**
```python
import streamlit as st
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="my_postgres_container",
    database="testdb",
    user="aaradhya",
    password="secret"
)
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT * FROM passengers;")
data = cursor.fetchall()

# Streamlit UI
st.title("🚆 Passenger Details")
st.table(data)

# Close connection
cursor.close()
conn.close()
```

## 🐳 Dockerizing the Streamlit App
### **8️⃣ Create a Dockerfile**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY main.py .
RUN pip install streamlit psycopg2
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### **9️⃣ Build the Docker Image**
```bash
docker build -t streamlit_app .
```

### **🔟 Run the Streamlit Container**
```bash
docker run --name my_streamlit_container --network my_postgres_network -p 8501:8501 -d streamlit_app
```

## 🔗 Access the Application
Open a browser and visit:
👉 **[http://localhost:8501](http://localhost:8501)**

Below is a screenshot:

![Passenger Details](Screenshot%202025-03-19%20at%208.13.22%E2%80%AFPM.png)


