# Use Python 3.12 as base image
FROM python:3.12

# Install pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean

# Show Python and pip versions
RUN python3 --version
RUN pip3 --version

RUN mkdir /app
WORKDIR /app

# Copy script to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run your application
# CMD ["python", "app.py"]
