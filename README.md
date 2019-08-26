### Git Installation
```
# Install Git
$ sudo apt install git

# Checking the installation
$ git --version

# Git Configuration
$ git config --global user.name "krakowiakpawel9"
$ git config --global user.email "krakowiakpawel9@gmail.com"

# Generate SSH Key
$ ssh-keygen -t rsa -b 4096 -C "krakowiakpawel9@gmail.com"
# $ eval "$(ssh-agent -s)"
# $ ssh-add ~/.ssh/id_rsa

# Checking configuration
$ ssh -T git@github.com

# Clone existing repository
$ git clone "https://github.com/krakowiakpawel9/config-python.git"

# Check remote url
$ git remote -v

# Set SSH
$ git remote set-url origin git@github.com:krakowiakpawel9/config-python.git
```

### Python - Environment Management - Linux (Ubuntu)

```
# Run python
$ python3

# Display python path
$ which python3

# Display python path with sys package
$ python3
>>> import sys
>>> sys.executable
```

### Anaconda Installation
```
# Go to https://www.anaconda.com/distribution/
# Find the latest Linux version, download and run bash script
$ bash Anaconda3-2019.07-Linux-x86_64.sh
# Default Location: /home/user/anaconda3
# Enter 'yes' two times during the installation
# Verify your installation
$ which python3
```

### Conda - Virtual Environment
```
# Checking version
$ conda --version

# Conda Configuration
$ conda config --show

# Update conda
$ conda update conda

# Display all environments 
$ conda env list
$ conda info --envs

# Display all available packages
$ conda list

# Create new environment with specific version of python
# Default location:
#    /home/user/anaconda3/envs/my_app
$ conda create --name my_app python=3.6

# Activate the environment
$ conda activate my_app

# List all packages in the environment
$ conda list

# Install package
$ conda install numpy

# Run command without requiring a user prompt (useful for scripts)
$ conda install -y numpy
$ conda install --yes numpy

# List all packages in the environment - checking installation 
$ conda list
$ conda list | grep numpy

# Remove package (deafult with dependencies)
$ conda remove numpy

# Remove only main package without dependencies
$ conda remove --force numpy

# Install many packages
$ conda install numpy pandas matplotlib

# Search for specific version
$ conda search numpy

# Install specific version
$ conda install numpy==1.16.0

# Uninstall package
$ conda uninstall numpy --name ENV_NAME

# Update all packages within an environment
$ conda update --all --name ENV_NAME

# Remove an environment
$ conda remove --name my_app --all

# Make an exact copy of an environment
$ conda create --clone old_env --name new_env

# Export an environment to a YAML file that can be read on Windows, macOS, Linux
$ conda env export --name ENV_NAME > env_name.yml

# Create an environment from the YAML file
$ conda env create --file env_name.yml

# Create an environment from the file named environment.yml in the current directory
$ conda env create

```

### Data Science
```
# Create virtual environment
$ conda create --name science python=3.6

# Install Jupyter Notebook
$ conda install -c anaconda jupyter
$ which jupyter

# Run Jupyter Notebook
$ jupyter-notebook

# Install Jupyter Lab
$ conda install -c conda-forge jupyterlab
$ which jupyter-lab

# Run Jupyter Lab
$ jupyter-lab

# Open Jupyter from the console
$ which jupyter
$ jupyter-notebook

# Install package from jupyter 
!conda install -y numpy

# Install Spyder
$ conda install -c anaconda spyder

# Run Spyder
$ spyder
```
