#!/bin/bash




python3 backend.py &
cd App/ ; echo EXPO_PUBLIC_HOSTIP=$REACT_NATIVE_PACKAGER_HOSTNAME > .env 
npx expo start &

wait -n

exit $?