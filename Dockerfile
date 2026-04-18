FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Copy everything from GitHub into the container
COPY . /app

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# This tells the bot to look inside the "downloaded_files" folder
CMD ["python", "app.py"]
