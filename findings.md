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


# For course personnel 
If the course personnel wants to run this exercise all they need to do is run 


- "docker compose up --build"  

docker compose without hyphen(-)
