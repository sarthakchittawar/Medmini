FROM node:18-bookworm-slim

# ARG REACT_NATIVE_PACKAGER_HOSTNAME

WORKDIR /medmini
COPY . .



RUN mv build_utils/services.sh services.sh \
    && chmod +x services.sh \
    && apt-get update \
    # && apt install curl -y \
    && cd App && npm ci && cd .. \
    && apt-get update \
    && apt-get install python3 python3-pip -y \
    && rm -rf /usr/lib/python3.11/EXTERNALLY-MANAGED \
    && pip3 install torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu \
    && pip3 install transformers==4.34.1 langchain==0.0.324 Flask==3.0.0 flask-cors==4.0.0 chromadb==0.4.15 sentence-transformers==2.2.2 sentencepiece==0.1.99 

# SHELL ["/bin/bash", "--login", "-i", "-c"]
# SHELL ["/bin/bash", "--login", "-c"]




# EXPOSE 19000 19001 19002
EXPOSE 8081 5000


CMD ./services.sh



# todo
# use a smaller base image