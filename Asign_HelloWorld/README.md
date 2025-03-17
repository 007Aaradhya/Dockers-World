# Docker Hello World Basics

This repository demonstrates the basic usage of Docker by running a simple Python application inside a container. It includes Docker Compose configurations for easy setup and debugging.

## Prerequisites

Before running this project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started) - To create and run containers.
- [Docker Compose](https://docs.docker.com/compose/) - To manage multi-container applications.
- [Git](https://git-scm.com/) - To clone the repository.

## Installation and Usage

### Clone the Repository

First, clone this repository to your local machine using:

```bash
git clone https://github.com/007Aaradhya/Docker_HelloWorld_Basics.git
cd Docker_HelloWorld_Basics
```

### Build and Run the Docker Container

To build and run the application using Docker Compose, execute:

```bash
docker-compose up --build
```

This will:
- Build the Docker image using the provided `Dockerfile`.
- Start the `asignhelloworld` container.

To stop the container, run:

```bash
docker-compose down
```

### Running in Debug Mode

If you want to debug the application, use:

```bash
docker-compose -f docker-compose.debug.yml up --build
```

This will:
- Install `debugpy` inside the container.
- Expose port `5678` for debugging.

## Project Structure

```
Docker_HelloWorld_Basics/
│── app.py                   # Main Python application
│── Dockerfile               # Docker configuration file
│── requirements.txt         # List of dependencies
│── docker-compose.yml       # Default Docker Compose configuration
│── docker-compose.debug.yml # Debugging setup with debugpy
└── README.md                # Project documentation
```

### Explanation of Each File

#### 1. `app.py`
The main Python script that runs inside the container. You can modify it to extend functionality.

#### 2. `Dockerfile`
Defines the containerized environment:

1. **Uses a Python Base Image:**
   ```Dockerfile
   FROM python:3.9
   ```

2. **Sets the Working Directory:**
   ```Dockerfile
   WORKDIR /app
   ```

3. **Copies Files into the Container:**
   ```Dockerfile
   COPY . .
   ```

4. **Installs Dependencies:**
   ```Dockerfile
   RUN pip install -r requirements.txt
   ```

5. **Defines the Default Command:**
   ```Dockerfile
   CMD ["python", "app.py"]
   ```

#### 3. `requirements.txt`
Contains dependencies required for the Python application. Update it using:
```bash
pip freeze > requirements.txt
```

#### 4. `docker-compose.yml`
Defines a service called `asignhelloworld` that builds the image and runs the container.

#### 5. `docker-compose.debug.yml`
An alternative Compose file that:
- Installs `debugpy`.
- Opens port `5678` for remote debugging.

## Useful Docker Commands

Here are some helpful commands to manage Docker containers and images:

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
docker rmi asignhelloworld
```

### List all Docker images
```bash
docker images
```

## Author

[Aaradhya Agrawal](https://github.com/007Aaradhya)

# Asign HelloWorld Project
