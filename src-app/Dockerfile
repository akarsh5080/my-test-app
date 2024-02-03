# Use the official Python image as the base image
FROM --platform=linux/amd64 python:3.9

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the application code to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Command to run the application
CMD ["/usr/local/bin/python3", "app.py"]

