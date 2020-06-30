#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:43:51 2019

@author: riteshsharma
"""

import NGrams
import sys


class NGramHash(object):

    SALT_FILE_NAME = "A.txt"
    N_GRAMS_SIZE = 3

    """
    Get character n-grams from salt file
    """
    @staticmethod
    def get_salt_file_character_n_grams():
        char_n_grams = NGrams.get_character_n_grams(NGramHash.SALT_FILE_NAME, NGramHash.N_GRAMS_SIZE)
        char_n_gram_set = set()
        for n_gram in char_n_grams:
            char_n_gram_set.add(n_gram)
        return list(char_n_gram_set)

    def __init__(self, hash_function_number, number_of_items_to_estimate_frequency_for, salt_n_grams):
        self.salt_n_grams = salt_n_grams
        self.hash_function_number = hash_function_number
        self.number_of_items_to_estimate_frequency_for = number_of_items_to_estimate_frequency_for

    """
    Get the hash value for a character
    """
    def get_stream_item_hash(self, character_to_hash):

        try:
            salt_for_hash_function = self.salt_n_grams[self.hash_function_number]
            return hash((str(salt_for_hash_function) + character_to_hash)) % \
                   self.number_of_items_to_estimate_frequency_for

        except IndexError:
            print("Index " + str(self.hash_function_number) + " is outside the range")
            sys.exit()

    """
    Functions needed to use class as a key
    """
    def __hash__(self):
        return hash((self.hash_function_number, self.number_of_items_to_estimate_frequency_for))

    def __eq__(self, other):
        return self.hash_function_number == other.hash_function_number and \
               self.number_of_items_to_estimate_frequency_for == other.number_of_items_to_estimate_frequency_for

    def __ne__(self, other):
        return not(self == other)