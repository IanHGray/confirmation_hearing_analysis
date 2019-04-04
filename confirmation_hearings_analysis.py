#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:57:05 2019

@author: iangray
"""

import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
import numpy as np
import collections
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
from contractions import CONTRACTION_MAP
from confirmation_hearing_stopwords import hearing_stopwords

warnings.filterwarnings('ignore')

stopword_list = nltk.corpus.stopwords.words('english') + hearing_stopwords

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens

def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def expand_contractions(text, contraction_mapping):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), flags = re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction
    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def remove_speaker_headers(text):
    text = text.split('.', 1)[1]
    return text

def normalize_corpus(corpus):
    normalized_corpus = []
    for text in corpus:
        text = text.lower()
        text = remove_special_characters(text)
        text = expand_contractions(text, CONTRACTION_MAP)
        text = remove_stopwords(text)
        normalized_corpus.append(text)
    return normalized_corpus
    
def get_top_words(nominee, speaker = None, num_words = 20):
    data = pd.read_excel('confirmation_hearings.xlsx')
    data['Hearing'] = data['Hearing'].str.lower()
    filtered = data[data['Hearing'].str.contains(nominee.lower())]
    if speaker is not None:
        filtered['Speaker and title'] = filtered['Speaker and title'].str.lower()
        dataframe = filtered[filtered['Speaker and title'].str.contains(speaker.lower())]
    else:
        dataframe = filtered
        
    dataframe['Statements'] = map(remove_speaker_headers, dataframe['Statements'])
    content = dataframe['Statements'].tolist()
    normalized_corpus = normalize_corpus(content)
    joined = []
    for text in normalized_corpus:
        words = nltk.word_tokenize(text)
        for word in words:
            joined.append(word)
    
    wordcount = {}
    
    for word in joined:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    
    #for word, count in word_counter.most_common(num_words):
    #    print word, ":", count
    
    lst = word_counter.most_common(num_words)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    w = df['Word'].tolist()
    c = df['Count'].tolist()

    plt.barh(range(len(w)), c)
    plt.yticks(range(len(c)), w)    
    plt.title('Word Frequency')

def main():
    nominee = raw_input("Which nominee are we looking at?" )
    speaker = raw_input("Any particular speaker we want to analyze? (If not, type 'None') ")
    if speaker == 'None' or speaker == 'none':
        speaker = None
    get_top_words(nominee, speaker)
    
if __name__ == '__main__':
    main()