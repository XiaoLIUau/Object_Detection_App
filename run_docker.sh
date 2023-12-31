#!/bin/bash

# Source environment variables from the file
source ./set_env.sh

# Run the Docker container with environment variables
docker run 
--device=/dev/video0
-e EMAIL_USER="$EMAIL_USER" 
-e EMAIL_PASSWORD="$EMAIL_PASSWORD" 
-p 5000:5000 
my_detection_app
