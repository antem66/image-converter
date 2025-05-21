# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the cache to keep the image size smaller
# --trusted-host pypi.python.org: Sometimes helpful in restrictive network environments, or for consistency
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app.py .

# Make port 8080 available to the world outside this container
# The app uses the PORT environment variable, defaulting to 8080.
ENV PORT 8080
EXPOSE 8080

# Define environment variable for Flask to run in production mode (optional, but good practice)
# For Gunicorn, you might set WORKERS or other Gunicorn-specific variables here.
# For a simple Flask dev server, this is not strictly necessary but doesn't hurt.
ENV FLASK_ENV production

# Run app.py when the container launches
# The app.py script is configured to listen on 0.0.0.0 and the PORT env variable.
CMD ["python", "app.py"]