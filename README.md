

Code for finetuning xsum and 5 different experts for tatoeba(translation).
The code of this repository is based on https://github.com/seonghyeonye/Flipped-Learning
## Setting

The following command will clone the project:
```
git clone https://github.com/doeyoungkim/multilingual_finetune.git
```

Before experimenting, you can make a virtual environment for the project.
```
conda create -n zeroshotlm python=3.8
conda activate zeroshotlm
pip install -r requirements.txt
```

## Dataset download
First, go to the data folder
```
cd data
```
Then, download 5 links under data folder
https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-kor.tar
https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-spa.tar
https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-fra.tar
https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-jpn.tar
https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-zho.tar
After downloading, preprocess each data into json files.
For example, when preprocessing korean task, you should run 
```
python tatoeba_preprocess_total.py kor
```
## Training
We provide commands for all our experiments in README.md under T0 directory. Check [this](./T0/README.md) out!




