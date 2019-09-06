When you work with python and pip you may **face with problem of SSL certificates verification** working between your machine 
and internet connection. To override this problem you should make python packages hosts to be trusted. 
Below you will find commands that allows you to override trusting hosts.

### Install package 
```
pip3 install --trusted-host=pypi.python.org  \
    --trusted-host=pypi.org \
    --trusted-host=files.pythonhosted.org <package>[==<vsersion>] [--user] [--force]
```

If you have other hosts during the installation you must add them as *--trusted-host*

Parameter *==\<version\>* is optional and means that specific package version will be installed

Parameter *--user* is optional and means that package should be installed for user that runs command (user home directory/.local)

Parameter *--force* is optional and means that package should be reinstalled if it is already installed

### Upgrade package
```
pip3 install --trusted-host=pypi.python.org \
    --trusted-host=pypi.org \
    --trusted-host=files.pythonhosted.org --upgrade <package>[==<version>] [--user] [--force]
```
### Upgrade pip 
```
pip3 install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade setuptools
pip3 install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade pip wheel
```
If not works, use this:
```
python -m pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade setuptools
python -m pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade pip
```
### Upgrade pip using Jupyter Notebook
```

!pip3 install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade setuptools --user
!pip3 install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade pip wheel --user
```

