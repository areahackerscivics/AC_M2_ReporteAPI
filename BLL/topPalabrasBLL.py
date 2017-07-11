

import sys, os
import numpy as np
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

def getTopPalabrasBLL(anyo, mes):

    tweets = getTweetsClasificados(anyo, mes)

    '''
        Para capturar menciones @ , hashtags # , y webs http://...
        ((RT)|(@[a-z:]*)|(http:\/\/[a-z.]*)|(#[a-zA-Z]*)|( )|(!))|(:D)

        Para capturar solo las palabras del tweet
        (?<![#@])\b\w+\b

        [a-zñáéíóúàèìòù]
    '''

    '''
    Esta expresión regular busca evitar las palabras con hashtags y menciones (#@) y
    capturar palabras en valenciano como  il·lusió   o   anem-nos
    '''
    pattern = r"(((?<![#@])\b\w+((-|·|')\w+)+\b)|((?:^|(?<=\s))\w+(?=\s|$)))"
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
