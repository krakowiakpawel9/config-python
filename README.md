### Python - Environment Management - Linux (Ubuntu)

```# Run python
$ python
$ python3

# Display python path
$ which python
$ which python3

# Display python path with sys package
$ python3
>>> import sys
>>> sys.executable

# Display all environments 
$ conda env list
$ conda info --envs

# Display all available packages
$ conda list

# Create new environment with specific version of python
# Default location:
#    /home/user/anaconda3/envs/my_app
$ conda create --name my_app python=2.7

# Activate the environment
$ conda activate my_app

# List all packages in the environment
$ conda list

# Install package
$ conda install numpy
$ conda install -y numpy

# List all packages in the environment - checking installation 
$ conda list

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
```

### Data Science
```# Create virtual environment
$ conda create --name science python=3.6

# Install Jupyter Notebook
$ conda install -c anaconda jupyter
$ which jupyter

# Install JupyterLab
$ conda install -c conda-forge jupyterlab

# Open Jupyter from the console
$ which jupyter
$ jupyter-notebook

# Install package from jupyter 
!conda install -y numpy

# Install Spyder
$ conda install -c anaconda spyder```
