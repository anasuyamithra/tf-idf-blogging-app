#!/usr/bin/env python
# coding: utf-8


# >> Importing Modules
import string
import collections
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os
import json
import sys
nltk.download('stopwords')
nltk.download('punkt')


# >> Initializing classes
s_words = list(stopwords.words('english'))
s_words.extend(['miro', 'max', 'medium', 'www', 'https', 'com'])


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = str(str(ROOT_DIR) + '/array.txt')

with open(file_name, 'r',encoding = 'utf-8') as file:
    data = file.read()
dataset = data.split(',/n"')


# >> Preprocessing Function
def preprocessing(text):
    # >>> Lowering the text
    text = text.lower()
    
    # >>> Removing Punctuation
    text_p = "".join([char for char in text if char not in string.punctuation])

    # >>> Word Tokenization
    words = word_tokenize(text_p)
    
    # >>> Removing Stopwords
    filtered_words = [word for word in words if word not in s_words]
    
    # >>> Stemming
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    
    return stemmed

# >> Function to find dot product of two vectors
def dot_product(vector_1, vector_2):
    counter = 0
    
    for word in vector_1[0].keys():
        if word in vector_2[0].keys():
            counter += vector_1[0][word]*vector_2[0][word]
    
    return(counter/(vector_1[1]*vector_2[1]))
        
# >> Function to determine similarity using Cosine Similarity
def cosine_similarity(query, dataset):
                        
    # >>> Applying preprocessing function to query
    query = preprocessing(query)
    counter = collections.Counter(query)
    count = dict(counter)
    mag_2 = sum(x**2 for x in counter.values())
    
    # >>> Vectorized query with word count and magnitude
    q_vector = (count, np.sqrt(mag_2))
    
    # >>> Dictionary of similarity scores
    score = {}
    for i in range(len(dataset)):
        score[i] = dot_product(q_vector, dataset[i])

    score = sorted(score.items(), key = lambda x: x[1], reverse = True)
    return score
            
# >> Preprocessing the Dataset
preprocessed = []
for article in dataset:
    temp = preprocessing(article)
    counter = collections.Counter(temp)
    mag_2 = sum(x**2 for x in counter.values())
    preprocessed.append((dict(counter), np.sqrt(mag_2)))


# In[23]:

Articles = cosine_similarity(sys.argv[1], preprocessed)
some = list(Articles)
# some.append(sys.argv[1])

indices = []

for i in range(4):
    indices.append(some[i][0])

answer = {}

answer['scores'] = indices



print(json.dumps(answer))