# Python setup
FROM python:3-slim AS python-env
WORKDIR /app
COPY requirements.txt .  
RUN pip install -r requirements.txt
COPY ./App /app/App  # Fix: Ensure App is copied inside /app
CMD ["python", "/app/App/app.py"]

# Node.js setup
FROM node:18 AS node-env
WORKDIR /app
COPY ./App /app/App  # Fix: Ensure App is copied inside /app
CMD ["node", "/app/App/index.js"]
