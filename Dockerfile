# Use Python 3.12 as base image
FROM python:3.12

# Install pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean

# Uncomment this if you are not using a DevContainer.
# RUN mkdir /app
# WORKDIR /app
# COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Uncomment this if not using a DevContainer. This will run the script on container start-up. Output can be viewed in Docker Desktop.
# CMD ["python", "mqtt-connect.py"]
