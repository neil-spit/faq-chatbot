# Use the official Python image.
FROM python:3.10-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container.
COPY . .

# Expose the port that the app will run on.
EXPOSE 8000

# Define the command to run the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
