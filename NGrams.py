#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:44:55 2019

@author: riteshsharma
"""

from nltk.util import ngrams
import nltk


def get_character_n_grams(file_name, n):

    with open(file_name) as file_handle:
        for file_snippet in file_handle:
            file_n_grams = ngrams(file_snippet, n)
            for n_gram in file_n_grams:
                yield(n_gram)