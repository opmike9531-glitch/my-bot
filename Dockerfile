FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium
EXPOSE 10000
CMD ["python", "app.py"]
