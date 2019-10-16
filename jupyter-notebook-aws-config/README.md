### How to set up Jupyter Notebook on EC2 instance

1. Set up your instance (Ubuntu 18.04) with the security group (sg.JPG).

2. Put your keys to the rigth folder, e.g. `~/jupyter-keys.pem`
```
$ sudo chmod 400 jupyter-keys.pem
```
3. Connect to your instance using SSH
```
$ ssh -i 'jupyter-keys.pem' ubuntu@PublicDNS
```
4. Download Anaconda, for example
```
$ wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
$ bash Anaconda3-2019.07-Linux-x86_64.sh
```
and follow the instructions.
Default path: `/home/ubuntu/anaconda3`

5. Check the Anaconda Installation
```
$ source .bashrc
$ which python3 -> /home/ubuntu/anaconda3/bin/python3
```

6. Create a password for jupyter notebook
```
$ ipython
In [1]: from IPython.lib import passwd
In [2]: passwd()
Enter password:
Verify password:
Out [2]: 'sha1:evcdjnc'
In [3]: exit
```
7. Create config profile
```
$ jupyter notebook --generate-config
```
8. Create certificates for https
```
$ cd 
$ mkdir certs
$ cd certs
$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
$ sudo chown $USER:$USER /home/ubuntu/certs/mycert.pem
```

9. Configure Jupyter
```
$ cd 	~/.jupyter
$ vim jupyter_notebook_config.py
```
and insert the following
```
c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook

# Notebook config
c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem' #location of your certificate file
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False  #so that the ipython notebook does not opens up a browser by default
c.NotebookApp.password = u'sha1:evcdjnc'  #the encrypted password we generated above
# Set the port to 8888, the port we set up in the AWS EC2 set-up
c.NotebookApp.port = 8888
```
save and go to home directory.

10. Create directory for notebooks
```
$ mkdir Notebooks
$ cd Notebooks
```
11. Start Jupyter Notebook
```
$ jupyter notebook
```
