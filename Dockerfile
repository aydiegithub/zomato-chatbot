# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV CHAINLIT_HOST=0.0.0.0
ENV CHAINLIT_PORT=10000
# GROQ_API_KEY will be injected at deploy time

# Start the ChainLit app
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "10000"]
