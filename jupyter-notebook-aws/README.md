### How to configure Jupyter Notebook instance on EC2

**Step 0.** Create key pair. For example spark-keys.pem  
**Step 1.** Lanuch EC2 instance and connect via SSH (Ubuntu Server 18.04)  
**Step 2.** Run the following commands:
```
$ sudo apt update

$ sudo apt install python3-pip -y
$ sudo apt install jupyter-notebook -y

$ sudo apt install openjdk-8-jre-headless -y
$ java -version

$ sudo apt install scala -y
$ scala -version

$ pip3 install py4j

$ wget https://archive.apache.org/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
$ sudo tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz

$ pip3 install findspark

$ mkdir ~/certs
$ cd certs
$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
$ sudo chmod 777 mycert.pem

$ jupyter notebook --generate-config
```
Open `~/.jupyter/jupyter_notebook_config.py` and paste it:
```
c = get_config()
c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
```

Open jupyter notebook instance and type into it:
```
import findspark
findspark.init('/home/ubuntu/spark-2.4.4-bin-hadoop2.7')
import pyspark

```
