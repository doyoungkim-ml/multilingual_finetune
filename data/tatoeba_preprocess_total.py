import time
import random
import sys
from tqdm import tqdm
def main(name):
    dir = "../release/v2021-08-07/eng-"+name
 
    data = []
    f = open(f"./{dir}/train.src", 'r')

    temp = f.readlines()
    list = sorted(random.sample(range(len(temp)), 500000))
    print((list))
    print(name)
    for idx in list:
        data.append({'en': temp[idx]})

    f.close()
    cnt=0
    f = open(f"./{dir}/train.trg", 'r')
    temp = f.readlines()
    for idx in list:
        data[cnt][name]=temp[idx]
        cnt+=1
    f.close()

    import json
    json_data = {
        "data": data
    }
    with open(f'./{dir}/tatoeba_{name}.json', 'w', encoding='utf-8' ) as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
def main2(name):
    dir = "../release/v2021-08-07/eng-"+name
    data = []
    with open(f"./{dir}/test.src", 'r') as f, open(f"./{dir}/test.trg", 'r') as g:
        for src, tgt in zip(f, g):
            
            data.append({'en': src, name: tgt})



    import json
    json_data = {
        "data": data
    }
    with open(f'./{dir}/tatoeba_val_{name}.json', 'w', encoding='utf-8' ) as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    main(sys.argv[1])
    main2(sys.argv[1])