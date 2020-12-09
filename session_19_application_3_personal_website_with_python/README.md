# First Flask Application

## First of all, install virtualenv

```sh
sudo apt-get install -y python3-venv
pip3 install virtualenv
```

### Create an virtual environment to isolate your environment

```sh
python -m venv virtual
```

## To start playing with Flask, just install it

```sh
virtual/bin/pip3 install flask
virtual/bin/pip3 install gunicorn
```

## To use the virtual environment, just:

```sh
virtual/bin/python script.py
```

## Install snap if necessary

```sh
sudo rm /etc/apt/preferences.d/nosnap.pref
sudo apt update
sudo apt install snapd
```

## Install heroku toolbelt

```sh
sudo snap install --classic heroku
```

## How to use Heroku

```sh
heroku login
heroku create novinho
heroku apps
```
