# Docker Streamlit

This repository contains a Streamlit application that is containerized using Docker. The purpose of this project is to demonstrate how to deploy a Streamlit app inside a Docker container, making it easier to run and share without worrying about dependencies.

## Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started) - To containerize and run the application.
- [Git](https://git-scm.com/) - To clone the repository.
- [Python](https://www.python.org/) (if running locally without Docker)

## Installation and Usage

### Clone the Repository

To get started, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/007Aaradhya/Docker_Streamlit.git
cd Docker_Streamlit
```

### Install Dependencies (If Running Locally)

If you wish to run the Streamlit app without Docker, install the required dependencies using:

```bash
pip install -r requirements.txt
```

Then, run the Streamlit application:

```bash
streamlit run app.py
```

### Build the Docker Image

To create a Docker image of the Streamlit application, execute the following command:

```bash
docker build -t streamlit_app .
```

### Run the Docker Container

Once the Docker image is built, run a container using:

```bash
docker run -p 8501:8501 streamlit_app
```

Now, open your browser and go to:

```
http://localhost:8501
```

Your Streamlit application should now be running inside a Docker container.

## Project Structure

The repository contains the following files:

```
Docker_Streamlit/
│── app.py              # Streamlit application script
│── Dockerfile          # Docker configuration file
│── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

### Explanation of Each File

#### 1. `app.py`
This is the main application script that runs the Streamlit application. It defines the UI and logic of the web application.

#### 2. `Dockerfile`
The `Dockerfile` is used to containerize the Streamlit application. It includes the following steps:

1. **Use a Python Base Image:**
   ```Dockerfile
   FROM python:3.9
   ```
   This selects the Python 3.9 image as the base for the container.

2. **Set the working directory:**
   ```Dockerfile
   WORKDIR /app
   ```
   It sets the working directory inside the container to `/app`.

3. **Copy the project files:**
   ```Dockerfile
   COPY . .
   ```
   This copies all necessary files into the container.

4. **Install dependencies:**
   ```Dockerfile
   RUN pip install -r requirements.txt
   ```
   This installs the required Python packages.

5. **Expose the port and run the app:**
   ```Dockerfile
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```
   It specifies the default command to start the Streamlit app on port 8501.

#### 3. `requirements.txt`
This file lists all the required Python packages needed for the application, such as:

```
streamlit
pandas
numpy
matplotlib
``` 

These dependencies are installed when the Docker container is built.

## Useful Docker Commands

Here are some useful Docker commands to manage your container:

### List all running containers
```bash
docker ps
```

### Stop a running container
```bash
docker stop <container_id>
```

### Remove a container
```bash
docker rm <container_id>
```

### Remove an image
```bash
docker rmi streamlit_app
```

### List all Docker images
```bash
docker images
```

## Author

[Aaradhya Agrawal](https://github.com/007Aaradhya)


---


# 2-Docker Streamlit
