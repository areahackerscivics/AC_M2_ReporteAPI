#!/usr/bin/env python
# encoding: utf-8

import sys, os
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

from DAO.tweetClasificadoDAO import *

import nltk
from nltk.probability import *
import re
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words

stopwords_cat = get_stop_words('catalan')
palabrasIgnorar = ['ajuntamentvlc', 'http', 'https', 'www', 'i', 'q', 'd']

def getTopHashtagsBLL(anyo, mes):

    tweets = getTweetsClasificados(anyo, mes)

    '''
    Esta expresión regular busca los hashtags, tanto en castellano como en valenciano
    '''
    pattern = r"(#\w+((·|-|')\w+)*)"
    tokenizer = RegexpTokenizer(pattern)

    texto = []
    for tweet in tweets:
        textoTw = tweet['texto']
        textoTw = textoTw.strip()
        textoTw = textoTw.strip('\n')

        palabras = tokenizer.tokenize(textoTw.lower())
        lista = []
        for palabra in palabras:
            lista.append(palabra[0])

        texto += lista

    #Quitando stopwords
    stopwords = set(nltk.corpus.stopwords.words('spanish') + stopwords_cat + palabrasIgnorar)
    texto = [palabra for palabra in texto if palabra not in stopwords]


    fdist=FreqDist(texto)

    mcomunes = fdist.most_common(10)

    result = []
    for elem in mcomunes:
        result.append( {'palabra': elem[0], 'menciones': elem[1]} )

    return result
