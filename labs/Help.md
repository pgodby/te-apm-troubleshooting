# Docker Help
If you are unfamiliar with Docker, the following tips will help you work with the containers during the lab exercises.

## Tips
The Splunk OTEL Collector Docker image does not include any text editors. Perform the following steps to make changes to configuration files in this container:
1. Copy a file to your machine.
    ```
    docker cp splunk-otel-collector:/path/to/file/filename.extension /working_directory
    ```
1. Using any text editor, edit and save the file.
1. Copy the file back to the running container.
    ```
    docker cp /working_directory/filename.extension splunk-otel-collector:/path/to/file/filename.extension
    ```
1. Restart the container to apply the changes.

---
Use the following command to restart the specified container:
```
docker restart <container_name>
```

---
If you update environment variable files, use the following command to apply the changes and recreate any updated containers:
```
docker-compose up -d
```

---
If you need to use an interactive shell, use the following command to open a terminal in the specified container:
```
docker exec -it <container_name> sh
```
To leave the interactive shell, type:
```
exit
```

---
If you are finished with the lab exercises and want to clean up the lab environment (or start over), use the following commands to manage the Docker images and containers.
```
# kill all running containers
docker kill $(docker ps -q)

# delete all containers
docker rm -vf $(docker ps -a -q)

# delete all images
docker rmi -f $(docker images -a -q)
```

---
**Labs Exercises:** [1](Lab1.md) | [2](Lab2.md) | [3](Lab3.md) | [4](Lab4.md) | Help