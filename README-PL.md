## Instalacja Systemu Kontroli Wersji - GIT
```
# Instalacja Git'a
$ sudo apt install git

# Sprawdzenie poprawnosci instalacji
$ git --version

# Konfiguracja Git'a
$ git config --global user.name "krakowiakpawel9"
$ git config --global user.email "krakowiakpawel9@gmail.com"

# Wygenerowanie kluczy SSH
$ ssh-keygen -t rsa -b 4096 -C "krakowiakpawel9@gmail.com"
# $ eval "$(ssh-agent -s)"
# $ ssh-add ~/.ssh/id_rsa

# Sprawdzenie konfiguracji
$ ssh -T git@github.com

# Sklonowanie repozytorium
$ git clone "http://github.com/krakowiakpawel9/config-python.git"

# Sprawdzenie zdalnego url
$ git remote -v

# Ustawienie SSH
$ git remote set-url origin git@github.com:krakowiakpawel9/config-python.git
```
### Python - Zarzadzanie srodowiskami - Linux (Ubuntu)
```
# Uruchomienie Python'a
$ python3

# Wyswietlenie sciezki do Python'a
$ which python3

# Wyswietlenie sciezki do Python'a z poziomu interpretera
$ python3
>>> import sys
>>> sys.executable
```
### Conda - Srodowisko Wirtualne
```
# Sprawdzenie Wersji
$ conda --version

# Sprawdzenie konfiguracji
$ conda config --show

# Zaktualizowanie condy
$ conda update conda

# Wyswietlenie srodowisk
$ conda env list
$ conda info --envs

# Wyswietlenie wszystkich dostepnych bibliotek
$ conda list

# Utworzenie nowego srodowiska z podana wersja Python'a
# Domyslna lokalizacja:
#  /home/USER/anaconda3/envs/my_app
$ conda create --name my_app python=3.6

# Aktywacja srodowiska
$ conda activate my_app

# Wylistowanie wszystkich bibliotek w srodowisku
$ conda list

# Instalacja biblioteki
$ conda install numpy

# Instalacja biblioteki z akceptacja wsyzstkich dependencji
$ conda install --yes numpy
$ conda install -y numpy

# Sprawdzenie instlacji
$ conda list | grep numpy

# Usuniecie biblioteki
$ conda remove numpy

# Usuniecie biblioteki bez dependencji
$ conda remove --force numpy

# Instalacja wielu bibliotek
$ conda install numpy pandas matplotlib

# Wyszukanie konkretnej biblioteki
$ conda search numpy

# Instalacja konkretnej wersji biblioteki
$ conda install numpy==1.16.0

# Odinstalowanie biblioteki
$ conda uninstall numpy --name ENV_NAME

# Aktualizacja wszystkich bibliotek w srodowisku
$ conda update --all --name ENV_NAME

# Usuniecie srodowiska
$ conda remove --name my_app --all

# Utworzenie kopii srodowiska
$ conda create --clone OLD_ENV --name NEW_ENV

# Export srodowiska do pliku YAML
$ conda env export --name ENV_NAME > env_name.yml

# Utowrzenie srodowiska z pliku YAML
$ conda env create --file env_name.yml

# Utorzenie srodowiska z pliku nazwanego environment.yml w biezacym katalogu
$ conda env create
```
### Data Science
```
# Utowrzenie srodowiska wirtualnego
$ conda create --name science python=3.6

# Instlacja Jupyter Notebook
$ conda install -c anaconda jupyter
$ which jupyter

# Uruchomienie Jupyter Notebook
$ jupyter-notebook

# Instalacja Jupyter Lab
$ conda install -c conda-forge jupyterlab
$ which jupyter-lab

# Uruchomienie Jupyter Lab
$ jupyter-lab

# Instalacja biblioteki poprzez Jupyter Notebook, Spyder
!conda install -y numpy

# Instalacja Spyder
$ conda install -c anaconda spyder

# Uruchomienie Spyder
$ spyder
```



