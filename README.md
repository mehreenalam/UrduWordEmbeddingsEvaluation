# WordEmbeddings

**Project Title**: Comparative Analysis of Different Word Embedding Techniques

**Project Type**: Research-based

**Supervisor**: Ms. Mehreen Alam

**Group Members**:
- Abubakar Ijaz (i160123)
- Ali Nauman Qureshi (i160138)
- Muhammad Raafey Tariq (i160259)

This repo consists of all the code and documentation for this Final Year Project (FYP). The directory structure of the repo is as follows:

1. **Code** - contains the scripts and notebooks used to process the corpora, train the models and perform evaluations
2. **Evaluation** - contains the datasets used to evaluate the performance of our models
3. **Literature** - contains the research work relevant to our area of interest
4. **Paper** - contains the content of our research paper
5. **Summaries** - contains the summaries of the papers we studied in detail for our mid-evaluation

## Running Code Guidelines
### All files here can be run and used with Google Colab after adjusting the variables described below
### Data used to train these models can be found on the following link:
https://drive.google.com/drive/folders/1jzVDFuqtJtjz7n1l1Gx6Rx_RiEOLCgTn?usp=sharing
### Saved Models:
https://drive.google.com/drive/folders/1X3Q75LzDhEhrxj1nICTxSbP1PkqxV_N0?usp=sharing
### Code Files:

1. **counting_words.ipynb** - To run this file adjust path and file_name variables according to path of the data text file
2. **data_preprocessing.ipynb** - To run this file adjust input_file variable to name of file that is to be pre-processed
3. **train_word2vec.ipynb** - To run this file adjust path and file_name variables according to path of the data text file
4. **train_fasttext.ipynb** - To run this file adjust path, root and filename variables according to path of the data text file
5. **evaluating_urdu_models.ipynb** - Adjust variables base and paths under the paths section to load models
6. **evaluating_roman_urdu_models.ipynb** - Adjust variables base and paths under the paths section to load models
7. **evaluating_roman_urdu_models_sa.ipynb** - Adjust paths in defining paths section and also colab specific statements section to paths of saved models
8. **eval_bert_xnli.ipynb** - Model checkpoints for BERT are stored in GCP Buckets, furthermore XNLI dataset would have to be downloaded from: https://cims.nyu.edu/~sbowman/xnli/ to run this file
9. **extract_bert_embeddings_roman.ipynb** - This file can only be run through our account axclusively as it requires use of a saved model on GCP to which we have access.
10. **extract_bert_embeddings_urdu.ipynb** - This file can only be run through our account axclusively as it requires use of a saved model on GCP to which we have access.
11. **extract_elmo_embeddings_urdu.ipynb** - Variables such as vocab_file, options_file, weight_file, outfile, json_file have to be adjusted according to the Path of the saved Urdu Model in the link to the models provided above.
12. **train_bert.ipynb** - PRC_DATA_FPATH has to be adjusted according to the data file location, GCP access is required to run this file
13. **train_elmo.ipynb** - Path to corpus has to be adjusted in load_corpus call, model language to train on has to be selected in the beginning

## References
1. https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
2. https://raw.githubusercontent.com/devmount/GermanWordEmbeddings/master/visualize.py
3. https://github.com/tthustla/twitter_sentiment_analysis_part11/blob/master/Capstone_part11.ipynb
4. https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-11-cnn-word2vec-41f5e28eda74
5. https://towardsdatascience.com/pre-training-bert-from-scratch-with-cloud-tpu-6e2f71028379
6. https://github.com/stanfordnlp/GloVe
