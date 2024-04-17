# Git CI/CD on own server
This project automaticly updates any project on remote server when any git push is made to the repository. This is done by using a webhook that listens to the push event on the repository. The webhook sends a POST request to the server with the payload of the push event. The server then runs a script that updates the project on the server.

## Install
Use the install.sh script to setup on an ubuntu virtual machine. It will create the necessary services and directories.
```
curl -s https://raw.githubusercontent.com/USCC/USCC-Bot/master/install.sh | bash 
```

## Config
