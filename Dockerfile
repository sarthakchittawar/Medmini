FROM alpine:3.14

RUN sudo apt install conda
RUN conda env create -f ./build_utils/env.yml

COPY ./App
COPY ./backend.py
COPY ./dbGen.py
COPY ./medmini.py
COPY ./mashqa_data
COPY ./build_utils/run.sh

RUN conda activate medmini

RUN chmod +x run.sh
RUN run.sh