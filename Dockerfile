# Use the specific Playwright image that matches your current error logs
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory inside the container
WORKDIR /app

# Copy your files into the container
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Playwright browsers are installed correctly for this version
RUN playwright install --with-deps chromium

# Expose the port Flask runs on
EXPOSE 10000

# Start the application
CMD ["python", "app.py"]
