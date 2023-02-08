# Running the Application

## With Docker
To run the application using Docker, follow these steps:

1. Build the Docker image for the Python API application by executing the following command: `docker build -t python-api-app .`

2. Start a container from the Docker image and map port 5000 in the container to port 5000 on the host machine by executing the following command: `docker run -p 5000:5000 python-api-app`


## With Docker Compose
Alternatively, you can use docker-compose to run the application: `docker-compose up -d`


## Accessing the API

After following one of these methods, you can access the Python API application by making requests to `http://localhost:5000`. The API has the following endpoints:
1. Reverse endpoint:
`curl "http://localhost:5000/reverse?in=Hello%20world"`
2. Restore endpoint:
`curl "http://localhost:5000/restore"`



