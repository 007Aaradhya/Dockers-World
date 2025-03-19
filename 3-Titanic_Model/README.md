
### **Create the Required Files**
Use the following commands to create empty files:
```bash
touch Dockerfile requirements.txt main.py titanic_model.py
```

#### **`Dockerfile`**
```dockerfile
# Use a slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY titanic_model.pkl titanic_model.pkl

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### **Build and Run in Docker**
```bash
docker build -t titanic-prediction .
docker run -p 8502:8501 titanic-prediction
```
![Titanic Model](Screenshot%202025-03-19%20at%209.28.34%E2%80%AFPM.png)
---
