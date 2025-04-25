# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Set the environment variables (optional)
ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV BOT_TOKEN=your_telegram_bot_token

# Run the bot
CMD ["python3", "bot.py"]
