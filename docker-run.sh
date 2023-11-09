#!/bin/bash


docker pull medmini

docker run -it --rm -p 8081:8081 -p 5000:5000 -e REACT_NATIVE_PACKAGER_HOSTNAME=$(hostname -I | awk '{print $1}') -e EXPO_DEVTOOLS_LISTEN_ADDRESS="0.0.0.0" medmini