# Stage 1: Build stage
FROM python:3.12-slim AS build

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the build container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final runtime stage
FROM python:3.12-slim

# Set the working directory in the final container
WORKDIR /app

# Copy only the necessary files from the build container
COPY --from=build /app /app

# Expose the port your application will run on
EXPOSE 5000

# Run the Flask app with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

