FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgirepository1.0-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the current project files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on (e.g., Flask uses 5000)
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
