# >> Importing modules
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
import collections
import numpy as np
import collections
import sys
import json
import os
nltk.download('stopwords')
nltk.download('wordnet')

# >> Initializing classes
s_words = list(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')

s_words.extend(['miro', 'max', 'medium', 'www', 'https', 'com', 'nwebsites', 'link', 'doses'])
Lem = WordNetLemmatizer()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = str(str(ROOT_DIR) + '/array.txt')

with open(file_name, 'r',encoding = 'utf-8') as file:
    data = file.read()
dataset = data.split(',/n"')

index_of_edit = 1000

# for i in dataset:
#     if str(sys.argv[1]) in dataset[i]:
#         index_of_edit = i

# >> Preprocessing Function
def preprocessing(text):
    # >>> Lowering the text
    text = text.lower()
    text = ''.join(i for i in text if not i.isdigit())

    # >>> Stemming
    arr = tokenizer.tokenize(text)

    # >>> Removing Stopwords
    arr = [word for word in arr if not word in s_words]
    arr = [Lem.lemmatize(word) for word in arr]
    # for word in arr :
    #     lemword = Lem.lemmatize(word)
    return arr

# >> Document Frequency
def df(dataset):
    DF = {}
    for i in range(len(dataset)):
        for word in dataset[i]:
            try:
                DF[word].add(i)
            except:
                DF[word] = {i}
    return DF


# >> TF IDF Function
def tf_idf(dataset):
    N = len(dataset)
    tf_idf_score = {}
    for i in range(N):
        counter = collections.Counter(dataset[i])
        for token in np.unique(dataset[i]):
            tf = counter[token]/len(dataset[i])
            df = len(DF[token])
            idf = np.log(N/(df+1))
            tf_idf_score[i, token] = "{0:.5f}".format(tf*idf)
    return tf_idf_score


fin_dataset = []


for article in dataset:
    if article not in fin_dataset:
        fin_dataset.append(preprocessing(article))
    

DF = df(fin_dataset)
# corpus = list(DF.keys())
solved = tf_idf(fin_dataset)
# final = sorted(solved.items(), key=lambda x: x[1], reverse=True)
finalfinal = {}


for key in solved.keys():
    try:
        if key[0] == int(sys.argv[2]):
            finalfinal[key[1]] = solved[key]
    except:
        if key[0] == 0:
            finalfinal[key[1]] = solved[key]


sorted_scores = {}
sorted_score_temp = sorted(finalfinal, key=finalfinal.get, reverse=True)  # [1, 3, 2]
i = 0
for w in sorted_score_temp:
    if i in range(5):
        sorted_scores[w] = finalfinal[w]
        i += 1

answer = {}

answer['tags'] = list(sorted_scores.keys())

# answer['tags'] = int(sys.argv[2])

print(json.dumps(answer))
