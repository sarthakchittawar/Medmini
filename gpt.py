from transformers import pipeline,GPT2Model,GPT2Tokenizer,AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig
import torch


prompt = f'What should I do if I want to stop dialysis? \nAnswer: '

#### Base GPT2 unquantized
# quantized=False
# extreme_quantization=False
# low_cpu=True

# # tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# # model = GPT2Model.from_pretrained('gpt2',low_cpu_mem_usage=low_cpu,device_map='cpu',load_in_8bit=quantized,load_in_4bit=extreme_quantization)

# args={"low_cpu_mem_usage":low_cpu,"device":'cpu',"load_in_8bit":quantized,"load_in_4bit":extreme_quantization,"torch_dtype":torch.float32}
# pipe = pipeline('text-generation', model='gpt2',model_kwargs=args)

# output=pipe(prompt)




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
# output=pipe(prompt)







#### Finetuned GPT2 model
model = AutoModelForCausalLM.from_pretrained("SidhiPanda/gpt2-finetuned-megathon", trust_remote_code=True, torch_dtype=torch.float32)
tokenizer = AutoTokenizer.from_pretrained("gpt2", trust_remote_code=True)
inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=512)
output = tokenizer.batch_decode(outputs)[0]



print(output)
