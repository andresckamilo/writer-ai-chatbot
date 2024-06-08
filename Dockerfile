# Base image
FROM python:3.10-bullseye

# Update and install necessary packages
RUN apt-get update -y && mkdir /app
RUN apt-get install build-essential cmake python3-dev -y

# Copy application code
COPY . /app
WORKDIR /app

# Install poetry and dependencies
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

# Expose port (not strictly necessary as it will be set by Railway)
# EXPOSE 8080

# Entry point and command to run your application
ENTRYPOINT [ "writer", "run" ]
CMD [ "--host", "0.0.0.0", "--port", "${PORT}" ]
