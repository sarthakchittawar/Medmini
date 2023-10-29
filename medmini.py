from transformers import pipeline,GPT2Model,GPT2Tokenizer,AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig
import torch
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


def formatPrompt(prompt,context):
    fp=f'USE THE FOLLOWING PIECES OF CONTEXT TO ANSWER THE QUESTION.\nQuestion: {prompt}\nContext: {context}\nAnswer: '
    return fp



prompt = f'What are some tips to handle bipolar disorder?'


### RAG

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)


vectordb=Chroma(persist_directory='./chroma_db_train',embedding_function=hf)
print(vectordb._collection.count())

docs = vectordb.similarity_search(prompt,k=4)
print(len(docs))
# print(docs)
context=' '.join(d.page_content for d in docs)
print(context)


#### Base GPT2 unquantized
# quantized=False
# extreme_quantization=False
# low_cpu=True

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2',low_cpu_mem_usage=low_cpu,device_map='cpu',load_in_8bit=quantized,load_in_4bit=extreme_quantization)

## args={"low_cpu_mem_usage":low_cpu,"device":'cpu',"load_in_8bit":quantized,"load_in_4bit":extreme_quantization,"torch_dtype":torch.float32}
# args={"low_cpu_mem_usage":low_cpu,"device_map":'cpu',"load_in_8bit":quantized,"load_in_4bit":extreme_quantization,"torch_dtype":torch.float32}
# pipe = pipeline('text-generation', model='gpt2',model_kwargs=args)

# output=pipe(formatPrompt(prompt, context), max_length=1024)

# output=pipe(formatPrompt(prompt, ''), max_length=1024)



#### Base GPT2 quantized
# tokenizer = AutoTokenizer.from_pretrained("gpt2", trust_remote_code=True)
# tokenizer.pad_token = tokenizer.eos_token

# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.float16
# )

# model = AutoModelForCausalLM.from_pretrained(
#     "gpt2",
#     quantization_config=bnb_config,
#     trust_remote_code=True
# )
# model.config.use_cache = False

# pipe=pipeline('text-generation',model=model,tokenizer=tokenizer)
# output=pipe(formatPrompt(prompt,context))


#### Phi 1.5 quantized/unquantized
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

bnb_config = BitsAndBytesConfig(
     load_in_4bit=True,
     bnb_4bit_use_double_quant=True,
     bnb_4bit_quant_type="nf4",
     bnb_4bit_compute_dtype=torch.float16
 )

model = AutoModelForCausalLM.from_pretrained(
     "microsoft/phi-1_5",
     # quantization_config=bnb_config,
     trust_remote_code=True
 )

pipe=pipeline('text-generation',model=model,tokenizer=tokenizer)
output=pipe(formatPrompt(prompt,context))






#### Finetuned GPT2 model
# model = AutoModelForCausalLM.from_pretrained("SidhiPanda/gpt2-finetuned-megathon", trust_remote_code=True, torch_dtype=torch.float32)
# tokenizer = AutoTokenizer.from_pretrained("gpt2", trust_remote_code=True)
# inputs = tokenizer(formatPrompt(prompt,context), return_tensors="pt", return_attention_mask=False)

# outputs = model.generate(**inputs, max_new_tokens=45)
# output = tokenizer.batch_decode(outputs)[0]

##########

# output

print(output)