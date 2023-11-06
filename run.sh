if ! [ -f ./mashqa_data/med_db ]
then
    cd mashqa_data
    python format.py
    cd ..; python dbGen.py
fi

python backend.py
cd App; npx expo start
