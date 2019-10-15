### AWS Lambda + Serverless framework + Ubuntu 18.04 Configuration

1. Execute following commands:
```
$ sudo apt update
$ sudo apt install docker.io -y
$ sudo docker run hello-world

$ sudo apt install nodejs -y

$ sudo apt install npm -y

$ sudo npm install -g serverless

$ sls config credentials --provider aws --key <access_key_is> --secret <secret_access_key_id>
$ sls create --template aws-python3 --name web-service
```
