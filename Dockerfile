# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Update the package list and install required packages
RUN apt-get update && \
    apt-get install -y ffmpeg aria2 git wget pv jq python3-dev mediainfo && \
    rm -rf /var/lib/apt/lists/*

# Install the necessary Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Force reinstall brotli
RUN pip install --force-reinstall brotli

# Install and upgrade yt-dlp
RUN pip uninstall -y yt-dlp && \
    pip install yt-dlp && \
    pip install --upgrade yt-dlp

# Copy the rest of the application code
COPY . .

# Check the yt-dlp installation
RUN python3 -m pip check yt-dlp

# Verify yt-dlp version
RUN yt-dlp --version

# Run the application
CMD ["python3", "main.py"]



# FROM python:3.10.8-slim-buster
# RUN apt-get update -y && apt-get upgrade -y \
#     && apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# COPY . /app/
# WORKDIR /app/
# RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
# CMD gunicorn app:app & python3 main.py
