# Dockerfile for Flask app with Nginx
FROM python:3.9-alpine

# Set up Flask app
WORKDIR /app


# Copy the Flask app code into the container
COPY challenge .

RUN pip install --no-cache-dir -r requirements.txt


COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY flag.txt /flag.txt

# Expose ports
EXPOSE 1235 

# Start Supervisor to manage processes
CMD ["/start.sh"]  