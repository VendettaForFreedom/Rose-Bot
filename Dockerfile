# Specify the base image
FROM python:3.6

# Set the working directory in the Docker image
WORKDIR /usr/src/app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Make sure your script is executable
RUN chmod +x run_tg_bot.sh

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ./run_tg_bot.sh