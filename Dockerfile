# Use the Playwright image as the base image
FROM mcr.microsoft.com/playwright/python:v1.37.0-focal

# Set the working directory
WORKDIR /usr/src/app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*

# Download and install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /usr/src/app/miniconda && \
    rm miniconda.sh

# Add Conda executable to PATH
ENV PATH="/usr/src/app/miniconda/bin:${PATH}"

# Copy the Conda environment file (environment.yml) to the container
COPY Config/environment.yml .

# Create and activate the Conda environment
RUN conda env create -f environment.yml

# Activate the Conda environment
SHELL ["/bin/bash", "--login", "-c"]

# Set the Python path
ENV PATH="/usr/src/app/miniconda/envs/PythonWithPlaywrightVEnv/bin:${PATH}"

# Copy the rest of the application code to the container
COPY . .

# Run your Playwright tests or any other commands you need
# CMD ["python", "-m", "pytest", "-k", "test_demo_04"]
