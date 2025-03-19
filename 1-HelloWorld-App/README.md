# 🚀 Hello World App with Docker 🐳

## 📌 Introduction
This project demonstrates a simple **Hello World** application running inside a **Docker container**. It serves as a basic introduction to containerization and deploying lightweight applications using Docker.

## 🔧 Prerequisites
Before running this project, ensure you have:
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Basic knowledge of Docker commands

## 🏗 Steps to Run the App

### **1️⃣ Build the Docker Image**
```bash
docker build -t hello-world-app .
```
- This command creates a Docker image named **hello-world-app** using the `Dockerfile` in the project directory.

### **2️⃣ Run the Container**
```bash
docker run --rm hello-world-app
```
- This command starts a container from the **hello-world-app** image and prints `Hello, World!` to the console.
- The `--rm` flag ensures the container is removed after execution.

### **3️⃣ Verify the Output**
Expected output:
```bash
Hello, World!
```
🎉 Your app is successfully running inside a Docker container!

## 🛠 Modify and Extend
- Modify `app.py` or `index.html` (if applicable) to customize the output.
- Build and run the container again to see your changes in action.

## 🎯 Conclusion
✅ Learned how to create and run a simple app inside a Docker container.  
✅ Gained hands-on experience with `docker build` and `docker run`.  
✅ Ready to explore more advanced Docker concepts! 🚀

---

