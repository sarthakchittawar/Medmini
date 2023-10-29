from numba import jit
import numba.cuda
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from timeit import default_timer as timer
import torch
@jit
def summarize(input_text):
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"
    print(torch.cuda.get_device_name(0))

    a = input_text
    if (len(input_text.split(' ')) < 50):
        print(a)
        return a
        
    start = timer()
    
    # edit these
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
    
    input = tokenizer.encode(input_text, return_tensors="pt").to(dev)
    model = model.to(dev)
    min_l = 0
    if (int(len(input_text.split(' '))/3) > 150):
        min_l = 150
    else:
        min_l = int(len(input_text.split(' '))/3)
    output = model.generate(input, max_length=150, min_length=min_l, length_penalty=1.0, num_beams=5, early_stopping=True)
    # print(timer() - start)
    numba.cuda.profile_stop()
    a = tokenizer.decode(output[0])[8:][:-4]
    return a

