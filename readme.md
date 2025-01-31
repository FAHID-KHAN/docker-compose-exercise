# Findings Report

In this exercise, two services were built using Docker and Docker Compose, each implemented in a different programming language. **Service1** was written in Python and served as an HTTP server, while **Service2**, written in Go, provided system information accessible only by Service1 through the Docker network.

Both services retrieved and displayed the following information:
- **IP Address**: Each container had its own IP address assigned by Docker’s internal network.
- **Running Processes**: The `ps aux` command was used to list processes running inside each container.
- **Disk Space**: The `df -h /` command was used to gather disk space statistics.
- **Uptime**: Uptime was fetched from `/proc/uptime` and formatted for better readability in both services.

Service1 exposed port 8199 to the host system, allowing external HTTP requests. Service1 then made internal HTTP requests to Service2 to gather additional system data, demonstrating inter-container communication over Docker's virtual network.

Containers in this setup shared some resources with the host system:
- **Networking**: Each container was assigned a unique internal IP address, and Service1 was exposed to the host system on port 8199. The two containers could communicate via Docker’s bridge network.
- **File System**: The containers used a layered file system based on the host's disk space, evident in the disk space readings that showed the same available space across both containers.
- **Kernel and Process Management**: Both containers shared the host system’s kernel, allowing them to run commands like `ps aux` and read from `/proc/uptime`, which is part of the host system's process and uptime management.

# Use of LLM
LLM model gpt 3.5 was used to get the idea of go lang and the coding process of go lang to show different data similiar to python os library . Also the markdown was first written by me and then it was given to llm to refine the written item .


### NGINX Gateway with Load Balancing and Authentication

An NGINX gateway was configured to handle external requests, implementing the following features:
- **Load Balancing**: NGINX distributes requests across three instances of Service1 using a round-robin algorithm, balancing the load across the instances.
- **Basic Authentication**: Access to the application requires login credentials. The username and password are set as follows in login.txt file.
  
  
- **Web Interface**: A simple HTML interface is provided at `http://localhost:8198/static/index.html`, allowing users to interact with the application. The interface includes:
  - **REQUEST Button**: Sends a request to one of the Service1 instances (selected by the load balancer) and displays the response.
  - **STOP Button**: Attempts to stop all services and exit Docker Compose gracefully.


# For course personnel 
If the course personnel wants to run this exercise all they need to do is run 


- "docker compose up --build"  

docker compose without hyphen(-)

Also a curl output from the docker exefcise is given in the repo for better understanding of how the data is being showed .JQ was used for this if you want to test it on your host machine run this command to get pretty json output 

- "sudo apt-get install jq"



Extended Report of the project branch 


## GitLab CI/CD Pipeline  
A **CI/CD pipeline** was configured to automate:  

1️⃣ **Build Stage**:  
   - Builds Docker images for **Service1, Service2, and API Gateway**.  
   - Stores images as **artifacts** for later use.  

2️⃣ **Test Stage**:  
   - **Runs functional tests** for each service.  
   - Even if tests **fail**, the pipeline **continues** (`allow_failure: true`).  
   - Generates **JUnit test reports** for review.  

3️⃣ **Deploy Stage**:  
   - Deploys the application **only on the `main` and `project` branches**.  
   - Handles errors gracefully (`docker-compose up -d || true`).  

🚀 **Final Deployment** is accessible at: `http://localhost:8198`  

The repo link to here is https://compse140.devops-gitlab.rd.tuni.fi/fahid-khan/nginx-cicd-pipeline



# API Gateway Description

## Overview
The **API Gateway** serves as the central entry point for the system. It is responsible for:
- **Managing Requests**: Directing external requests to the appropriate services.
- **State Management**: Controlling the behavior of the system based on predefined states (`INIT`, `RUNNING`, `PAUSED`, `SHUTDOWN`).
- **Inter-Service Communication**: Facilitating communication between **Service1** (Python) and **Service2** (Go).

The API Gateway listens on **port 8197** and provides the following key functionalities.






