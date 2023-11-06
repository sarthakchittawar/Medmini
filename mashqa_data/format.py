import os
import json

# pick out some data from json file and make a new json
def make_json(path):
    with open('{}'.format(path), 'r') as f:
        data = json.load(f)

    f = open('sentences.txt'.format(path[:-5]), 'a')
    data = data['data']
    
    for i in range(len(data)):
        para = data[i]['paragraphs']
        for j in range(len(para)):
            sentences = para[j]['sent_list']
            for k in sentences:
                f.write(k)
                f.write('\n')
            f.write('\n\n')
    f.close()
    
l = os.listdir('.')
for i in l:
    if i.endswith('.json') and not i.startswith('new'):
        make_json(i)
        print('done {}'.format(i))