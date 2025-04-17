# Folders structure 
app
-- simple_time_service.py
-- Dockerfile
-- requirements.txt

# Install Dependencies for direct python file execution
apt update 
apt install python3-pip
pip install flask

# Python file run command
python3 simple_time_service.py

# Build the docker image
docker build -t flask-simple-time-service .
# Run the docker container 
docker run -p 5000:5000 flask-simple-time-service
