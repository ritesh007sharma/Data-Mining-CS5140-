#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:41:41 2019

@author: riteshsharma
"""
import HashFunctions
import unittest
import sys


class CountMinSketchFrequentItems(object):

    S1_FILE_NAME = "S1.txt"
    S2_FILE_NAME = "S2.txt"
    NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR = 10
    NUMBER_OF_HASH_FUNCTIONS = 5

    def __init__(self, stream_file_name, number_of_items_to_estimate_frequency_for, number_of_hash_functions):

        self.stream_file_name = stream_file_name
        self.number_of_items_to_estimate_frequency_for = number_of_items_to_estimate_frequency_for
        self.number_of_hash_functions = number_of_hash_functions
        self.salt_n_grams = HashFunctions.NGramHash.get_salt_file_character_n_grams()

        # Create the item counters as a dictionary with the hash function as the key
        self.item_counters = dict()
        for hash_function_counter in range(self.number_of_hash_functions):
            self.item_counters[HashFunctions.NGramHash(hash_function_counter,
                                                       self.number_of_items_to_estimate_frequency_for,
                                                       self.salt_n_grams)] = \
            [0] * self.number_of_items_to_estimate_frequency_for

        # Estimate the frequency counts
        self.__estimate_frequency_counts()

    # Estimate frequency counts
    def __estimate_frequency_counts(self):

        # Read each character from the stream
        for stream_character in self.__get_next_character_from_stream_file():

            # Repeat for each hash function find the counter that the character hashes to and increment it
            for hash_function in self.item_counters:
                self.item_counters[hash_function][hash_function.get_stream_item_hash(stream_character)] += 1

    # Return one character at a time from the file
    def __get_next_character_from_stream_file(self):

        with open(self.stream_file_name) as file_handle:
            for text_line in file_handle:
                for character in text_line:
                    yield character

    # Return the estimate of the item count
    def get_item_count_estimate(self, query_item):

        item_count_estimate = sys.maxsize

        # For each hash function
        for hash_function in self.item_counters:

            # The current count estimate is the value of the counter the query object hashes to
            current_item_count_estimate \
                = self.item_counters[hash_function][hash_function.get_stream_item_hash(query_item)]

            # Save the minimum count estimate
            if current_item_count_estimate < item_count_estimate:
                item_count_estimate = current_item_count_estimate

        # Return the minimum count estimate across all hash functions
        return item_count_estimate



class TestCountMinSketch(unittest.TestCase):

    def test_for_s1_and_s2(self):

        for file_name in [CountMinSketchFrequentItems.S1_FILE_NAME, CountMinSketchFrequentItems.S2_FILE_NAME]:

            count_min_sketch_frequent_items \
                = CountMinSketchFrequentItems(file_name,
                                              CountMinSketchFrequentItems.NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR,
                                              CountMinSketchFrequentItems.NUMBER_OF_HASH_FUNCTIONS)

            print("\nCounts for file " + file_name)

            for query_item in ['a', 'b', 'c']:
                print("Frequency of " + str(query_item) + " is "
                      + str(count_min_sketch_frequent_items.get_item_count_estimate(query_item)))

if __name__ == "__main__":
    unittest.main()