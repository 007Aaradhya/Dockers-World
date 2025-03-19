🚀 **Docker Volume Persistence: Bind Mounts on Linux Containers** 🐳

## 📌 Introduction
This experiment explores how **Docker bind mounts** enable data persistence across container lifecycles. By mounting a local directory into a container, files remain accessible even after the container is removed. This is useful for sharing data between containers or preserving important files.

## 🔧 Steps & Observations

### 🏗 Step 1: Running a Container with a Bind Mount

**Command Executed:**
```bash
docker run -dit --name my_alpine -v ~/docker_data:/data alpine:latest sh
```

### 🔍 What Happened?
- Docker pulled the `alpine:latest` image if not already available.
- A container named `my_alpine` was created.
- The `-v` flag mounted the local directory `~/docker_data` to `/data` inside the container.
- The container started a shell (`sh`) in detached mode.

---

### 📄 Step 2: Creating a File Inside the Bind Mount

Inside the container, a file was created using:
```bash
docker exec -it my_alpine sh -c "echo 'Hello, Aaradhya!' > /data/testfile.txt"
```

### 🔍 What Happened?
- A shell command executed inside the running container.
- A file `testfile.txt` was created inside `/data`, containing "Hello, Aaradhya!".
- Since `/data` is a bind-mounted directory, the file is actually stored in `~/docker_data` on the host.

---

### ✅ Step 3: Verifying the File Exists

To check the contents of the file:
```bash
docker exec -it my_alpine sh -c "cat /data/testfile.txt"
```
**Expected Output:**
```
Hello, Aaradhya!
```
This confirms the file was successfully created and persists outside the container. 🎉

---

### 🗑 Step 4: Removing the Container

The container was removed using:
```bash
docker rm -f my_alpine
```

### 🔍 What Happened?
- The container was forcefully stopped and deleted.
- However, the file `testfile.txt` remained in the host directory (`~/docker_data`).

---

### 🔄 Step 5: Creating a New Container with the Same Bind Mount

A new container was started with the same mount:
```bash
docker run -dit --name new_alpine -v ~/docker_data:/data alpine sh
```

### 🔍 What Happened?
- A new container named `new_alpine` was created.
- The same local directory (`~/docker_data`) was mounted to `/data`.

---

### 🔎 Step 6: Verifying File Persistence

To check if `testfile.txt` is still accessible:
```bash
docker exec -it new_alpine sh -c "cat /data/testfile.txt"
```
**Expected Output:**
```
Hello, Aaradhya!
```
This confirms that bind mounts persist data beyond a container’s lifecycle. 🔥

---

## 🎯 Conclusion
✅ Bind mounts ensure persistent data storage across container instances.
✅ Deleting a container does **not** remove data stored in a bind-mounted directory.
✅ Any new container with the same mount can access existing data.
✅ Useful for **sharing files** between containers and keeping important files safe.

---

## 🚀 Next Steps
🛠 Try **named volumes** (`docker volume create`) for managed persistent storage.
🐳 Experiment with bind mounts on different container images.
🔐 Explore file permissions and access control between host and container.

This experiment highlights the power of bind mounts in Docker. Keep experimenting and happy coding! 🚀


