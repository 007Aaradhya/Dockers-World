# MySQL Using Docker

This repository demonstrates how to set up and run a MySQL database inside a Docker container. It includes database initialization with a SQL script, Docker Compose configurations, and necessary commands to manage the container.

## Documentation

- [Docker](https://docs.docker.com/)
- [MySQL](https://dev.mysql.com/doc/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Installation

To set up MySQL using Docker, follow these steps:

### 1. Create the SQL File

The SQL script initializes the `college` database and a `students` table:

```sql
CREATE DATABASE college;
USE college;

CREATE TABLE students (
    id INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO students (FirstName, Surname) VALUES
("Aaradhya", "Agrawal"),
("Rashi", "Garg");
```

Save this file as `db_college.sql`.

### 2. Create the Dockerfile

Create a `Dockerfile` with the following content:

```Dockerfile
FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./db_college.sql /docker-entrypoint-initdb.d/
```

### 3. Deployment Using Docker

Now, follow these steps to deploy MySQL using Docker:

#### Step 1: Check Existing Containers
```bash
docker container ls -a
```

#### Step 2: Build the Docker Image
```bash
docker build -t mysql_db .
```

#### Step 3: List Created Images
```bash
docker images
```

#### Step 4: Run the Docker Image
```bash
docker run --name heuristic_williamson -d mysql_db
```

#### Step 5: Execute MySQL Commands Inside the Running Container
```bash
docker exec -it heuristic_williamson mysql -u root -p
```

(Enter the MySQL root password when prompted.)

#### Step 6: Verify the Database
```sql
SHOW DATABASES;
USE college;
SHOW TABLES;
SELECT * FROM students;
```

