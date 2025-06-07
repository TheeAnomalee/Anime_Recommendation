# This allows you to use the official Python image
FROM python:3.11-slim

# This is the working directory
WORKDIR /app

# Copy files
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expose port
EXPOSE 5000

# Run the app
CMD ["python", "-m", "app.webapp"]
