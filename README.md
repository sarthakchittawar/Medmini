# **MedMini**

## _Runs within_  **< 3GB RAM | 0 vRAM**   
## _Inference Time_ **< 3 sec** 
### A Lightweight architecture for an Answering System on medical data based on LLMs, designed to run on **edge devices**. 
### Entirely on-device processing 
### Model Size on Disk: 500 + 250 MB 

![Pipeline](./media/diagram.png)




## **Instructions for Setup**

1. `cd mashqa_data`
2. `python format.py`
3. `cd ..; python dbGen.py`

## **Instructions to run**
1. `cd App; npx expo start`
2. `python backend.py`

## **Future work**
1. Dockerisation of the project to allow it to run from any IP address without having to do many changes.
2. Improve the RAG algorithm without compromising on efficiency