# Use the specific Playwright version that matches your environment
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Python dependencies from your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the Chromium browser and all required system libraries
# This prevents the 'Executable doesn't exist' error
RUN playwright install --with-deps chromium

# Expose the port used by Render (10000)
EXPOSE 10000

# Start the Flask application
CMD ["python", "app.py"]
