# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Expose the desired port (replace 5000 with the actual port your app listens on)
EXPOSE 5000

# Set the entrypoint command to run the Flask app
CMD ["python", "runserver.py"]