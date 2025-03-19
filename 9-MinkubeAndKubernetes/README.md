Minikube with Docker on macOS ☸️

What is Minikube?
Minikube is a tool that helps you run a local Kubernetes cluster on your Mac. It’s perfect for testing Kubernetes without needing a cloud setup. It supports multiple drivers, including Docker, HyperKit, and VirtualBox.

What is Kubernetes? ☸️
Kubernetes is an open-source platform for managing and scaling containerized applications.

📦 Deploy applications in containers
📊 Scale applications up or down
🔄 Ensure high availability
🎯 Automate container management
✅ Step 1: Install Required Tools

1️⃣ Install Docker 🐋
Minikube requires Docker to run Kubernetes inside a container.

🔹 Install Docker Desktop → Download Here

After installation, start Docker Desktop and verify:

docker --version
2️⃣ Install Minikube 📦
Install Minikube via Homebrew:

brew install minikube
Verify installation:

minikube version
3️⃣ Install kubectl (Kubernetes CLI)
brew install kubectl
Verify installation:

kubectl version --client
✅ Step 2: Start Minikube with Docker Driver 🐳

Since you’re using macOS (ARM64), start Minikube with Docker:

minikube start --driver=docker
📌 This initializes Kubernetes inside Docker instead of a virtual machine.

Verify Minikube status:

minikube status
✅ Expected Output:

minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
✅ Step 3: Deploy an Application 🚀

Let’s deploy a simple Nginx web server inside Kubernetes.

1️⃣ Create an Nginx Deployment
kubectl create deployment nginx --image=nginx
2️⃣ Expose the Deployment 🔓
kubectl expose deployment nginx --type=NodePort --port=80
3️⃣ Get the Service URL 🔗
minikube service nginx --url
✅ Expected Output:

http://127.0.0.1:XXXXX
📌 Open this URL in a browser to see the Nginx welcome page! 🌍

✅ Step 4: Manage Kubernetes Cluster

1️⃣ Check Running Pods 📋
kubectl get pods
2️⃣ Scale the Deployment 📏
Scale to 3 replicas:

kubectl scale deployment nginx --replicas=3
Check again:

kubectl get pods
3️⃣ Delete the Deployment 🧹
To remove everything:

kubectl delete service nginx
kubectl delete deployment nginx
✅ Step 5: Stop and Delete Minikube 🗑️

1️⃣ Stop Minikube
minikube stop
2️⃣ Delete the Cluster
minikube delete
📌 This removes all Kubernetes resources and stops Minikube.

