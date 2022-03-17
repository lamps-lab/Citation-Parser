# citation-parser
A deep learning model using Transformer and CRF to solve citation parsing problem.

Dataset Used: [GIANT](https://github.com/BeelGroup/GIANT-The-1-Billion-Annotated-Synthetic-Bibliographic-Reference-String-Dataset)

### Model Architecture:
- Feature: Word Embedding & Character Embedding(from BiLSTM)
- Features are fed into transformer encoder layer which got attention module
- Outputs from encoder layer are passed through 2-layers of fully connected linear layer
- Output of linear layer is fed into CRF to find out the most possible tag

### Tokenization Details
Built custom tokenizer which labels each word according to the XML tag on the citation string. Considered all the punctuation as a seperate class.
Note: Removed DOI/URI from training data.

BIO tagging scheme is used for the labels.

## File Introduction

### Model trainer files

- Trainer/citation-parser-trainer.py [Main]
- Trainer/corpus.py [Loads datasets]
- Trainer/transformerModel.py [Architecture definition]


### Data preparation 

- Data Preprocessing/csv-downsampler.ipynb

This file is used to downsample GIANT dataset into the target number. You can define sample size to take from each CSV and save it (as csv). 

- Data Preprocessing/dataset-builder.ipynb

It has one part with tokenizer. It takes on a citaion string and returns list of token-label tuples for each sentence.
Another part(s) takes on CSV, read each citation string, send it to tokenizers and build text files. Each line has one token-label pair. Each CSV has one respective text file.

- Data Preprocessing/concat-text-files.ipnyb
Concats all the text files into one. There's a space between each sentence.

### Bash file
- script-trainer.sh
To run this on HPC: 
    
    sbatch script-trainer.sh
    
### Tokenizer
Tokenize a real-world reference string for prediction. 

You may need to create environment and install required modules for a successful run.

### Evalution 
- citation-parser-inference-block-token.ipynb

This file is used to evaluate test sets. First it loads the model from directory. You need to set up the path of your dataset for evaluation.



