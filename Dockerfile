FROM alpine:3.14

RUN sudo apt install conda
RUN conda env create -f env.yml

COPY ./App
COPY ./backend.py
COPY ./dbGen.py
COPY ./medmini.py
COPY ./mashqa_data
COPY ./utils/run.sh

RUN conda activate Megathon

RUN chmod +x run.sh
RUN run.sh