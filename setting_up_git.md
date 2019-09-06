### General
```
git config --global http.sslVerify false
git config --global user.name "<user name>"
git config --global user.email "<email>"
```
### Generate RSA key pair using ssh-keygen Linux command:
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
### Add public key to authorized keys file on server pn your machine
```
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```


