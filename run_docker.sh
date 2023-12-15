#!/bin/bash

# Source environment variables from the file
source ./set_env.sh

# Run the Docker container with environment variables
docker run -e EMAIL_USER="$EMAIL_USER" -e EMAIL_PASSWORD="$EMAIL_PASSWORD" -p 5000:5000 your_container_name
