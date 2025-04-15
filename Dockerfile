## DOckerfile app.py

# Use the official Python image for python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install the necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Set the environment variable to tell Flask that we are in production
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0

# Command to run the Flask app
CMD ["python", "app.py"]
