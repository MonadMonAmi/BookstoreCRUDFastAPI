# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV DATABASE_URL=""

# Copy the current directory into the container
COPY . .

# Set the command to run the application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
