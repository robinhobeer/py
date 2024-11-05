# Use the official Python image as the base image
FROM python:3.12.5

# Set the working directory in the container
WORKDIR /py

# Copy the application files into the working directory
COPY . /py

# Install the application dependencies
RUN pip install streamlit

# Define the entry point for the container
CMD ["python", "app.py", "runserver", "0.0.0.0:8000"]
