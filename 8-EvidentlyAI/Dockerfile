# Use Python 3.10 as base image
FROM python:3.10  

# Set the working directory  
WORKDIR /app  

# Copy requirements and install dependencies  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy all project files  
COPY . .  

# Expose Streamlit port  
EXPOSE 8501  

# Run the Streamlit app  
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
