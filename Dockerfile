FROM python:3.11.4-slim

# Install system dependencies including PostgreSQL development files
RUN apt-get update && apt-get install -y \
    postgresql-client \
    default-jre \
    postgresql-server-dev-all \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create necessary directories
RUN mkdir -p /data/download /data/extracted /data/converted

# Command to run the console version
CMD ["python", "src/A_Main.py"]