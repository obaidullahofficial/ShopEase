# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the application code (app.py) from the local environment to the container
COPY app.py .

# Install the Flask package required for running the web service
RUN pip install flask

# Expose port 5000 so the service is accessible from outside the container
EXPOSE 5000

# Set the default command to run the application
CMD ["python", "app.py"]
