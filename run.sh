#!/bin/bash

# setting environment variables
export REACT_NATIVE_PACKAGER_HOSTNAME=$(hostname -I | awk '{print $1}')
export EXPO_DEVTOOLS_LISTEN_ADDRESS="0.0.0.0"

# starting frontend and backend
python3 backend.py &
cd App/ ; echo EXPO_PUBLIC_HOSTIP=$REACT_NATIVE_PACKAGER_HOSTNAME > .env 
npx expo start &

wait -n

exit $?

