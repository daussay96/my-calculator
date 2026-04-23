# Start from an official Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all your project files into the container
COPY . .

# Tell Docker which port your app uses
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]