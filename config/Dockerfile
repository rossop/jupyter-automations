# Use an official Python runtime as a parent image
FROM python:3.10.8-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Create the env directory
RUN mkdir env

# Copy the requirements.txt file into the container at /usr/src/app/env
COPY ./env/requirements.txt ./env/

# Install system dependencies required for building certain Python packages like psutil
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r ./env/requirements.txt

# Install code-server (Visual Studio Code in the browser)
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Expose ports for Jupyter Notebook and code-server
EXPOSE 8889 8080

# Start code-server and Jupyter Notebook
CMD ["sh", "-c", "code-server --bind-addr 0.0.0.0:8080 & jupyter notebook --ip=0.0.0.0 --port=8889 --allow-root --NotebookApp.token='' --NotebookApp.password=''"]