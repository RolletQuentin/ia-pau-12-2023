# Use the official Python image as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app/backend

# Copy the current directory contents into the container at /app/backend
COPY backend/ .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the model
RUN python initmodel.py

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
