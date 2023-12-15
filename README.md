# Object_Detection_App
Detect object in camera streaming using Tiny VIT model

# SETUPS and RUN
## First setup Huggingface API key
Step 1: Create a file named named ***api_key_huggingface.txt***

Step 2: Save your huggingface api key in the file 

## Second setup build docker image
Build docker image using cmd below:
```
docker build -t my_detection_app .
```

## Third setup email credentials as environment variables and deploy the app
### Option 1: 
Step 1: Fill your email address and password in the file named ***set_env.sh***, using below code snip:
```
#!/bin/bash

# Fill sender's email address and password, and reciver's email address in corresponding '' below
export EMAIL_USER=''
export EMAIL_PASSWORD=''  
export RECIVER_EMAIL=''
```
Step 2: Run cmd `./run_docker.sh` in terminal

### Option 2:
Setup directly to pass the varibales in as parameters using following cmd:

```
docker run 
--device=/dev/video0 
-e EMAIL_USER='your_email@example.com' 
-e EMAIL_PASSWORD='your_password' 
-p 5000:5000 
my_detection_app
```

Note: remember to change 'your_email@example.com' and 'your_password' with your emial credentials before run the cmd

