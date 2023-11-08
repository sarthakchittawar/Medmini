#!/bin/bash

# updating repositories and installing curl
apt update
apt install curl -y

# installing node and npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
source ~/.bashrc
nvm install v18.13.0


# installing all node modules required
cd App
npm ci
cd ..


# setting up python deps
apt update
apt install python3.10 python3-pip -y
pip3 install torch --index-url https://download.pytorch.org/whl/cpu
pip3 install transformers langchain Flask flask-cors chromadb sentence-transformers sentencepiece


#todo
# pull the med_db

