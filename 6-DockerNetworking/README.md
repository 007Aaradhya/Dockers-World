# 🐳 Docker Bridge: Network Isolation & Connectivity  

## 📌 Objective  
The goal of this experiment, conducted by **Aaradhya Agrawal**, is to explore **network isolation in Docker containers**. We test how containers inside a **custom bridge network** can communicate, while those on **different networks remain isolated**.  

## 🌐 Introduction to Docker Networking  
Docker provides several networking options:  
- **Bridge Network (Default)** – Containers can communicate unless restricted.  
- **Custom Bridge Network** – Provides better control & name-based resolution.  
- **Host Network** – Containers share the host’s network.  
- **Overlay Network** – Used in multi-host Docker Swarm setups.  
- **Macvlan Network** – Assigns real MAC addresses to containers.  
- **None Network** – Completely disables networking.  

This experiment **focuses on a custom bridge network** for better security and performance.  

## ⚡ Why Use a Custom Bridge Network?  
✅ **Security** – Containers on different networks are isolated.  
✅ **Performance** – No overhead from host networking.  
✅ **DNS-Based Resolution** – Containers communicate via names.  
✅ **Control** – Define specific IP ranges and rules.  

---

## 🏗 Steps Performed  

### **1️⃣ Creating a Custom Bridge Network**
```bash
docker network create --driver bridge --subnet 192.168.1.0/24 --ip-range 192.168.1.100/25 aaradhya-bridge
```

### **2️⃣ Running Containers Inside the Network**
```bash
docker run -itd --net=aaradhya-bridge --name=aaradhya-database redis
docker run -itd --net=aaradhya-bridge --name=aaradhya-server-A busybox
```

### **3️⃣ Checking Container IPs**
```bash
docker network inspect aaradhya-bridge
```

### **4️⃣ Testing Communication**
```bash
docker exec -it aaradhya-database ping -c 4 192.168.1.101
docker exec -it aaradhya-server-A ping -c 4 192.168.1.100
```

### **5️⃣ Running an Isolated Container**
```bash
docker run -itd --name=aaradhya-server-B busybox
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' aaradhya-server-B
```

### **6️⃣ Testing Network Isolation**
```bash
docker exec -it aaradhya-database ping -c 4 172.17.0.2
```
🚨 **Expected Result:** Ping should **fail** because the containers are on different networks.

### **7️⃣ Confirming Network Isolation**
```bash
docker network inspect aaradhya-bridge
docker network inspect bridge
```

---
