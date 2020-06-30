#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:12:22 2019

@author: riteshsharma
"""
import unittest
class MisraGriesFrequentItems(object):

    S1_FILE_NAME = "S1.txt"
    S2_FILE_NAME = "S2.txt"
    NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR = 10

    def __init__(self, stream_file_name, number_of_items_to_estimate_frequency_for):

        # Save stream file name
        self.stream_file_name = stream_file_name

        # Save number of counters required (plus one)
        self.number_of_items_to_estimate_frequency_for = number_of_items_to_estimate_frequency_for

        # Dictionary to save labels and their counts
        self.labels_and_counters = dict()

    # Return one character at a time from the file
    def __get_next_character_from_stream_file(self):

        with open(self.stream_file_name) as file_handle:
            for text_line in file_handle:
                for character in text_line:
                    yield character

    # Estimate the count for the k most occurring characters
    def estimate_character_counts(self):

        # Read each character from the stream
        for stream_character in self.__get_next_character_from_stream_file():

            # Increment the counter if the label was found
            if stream_character in self.labels_and_counters:

                self.labels_and_counters[stream_character] += 1

            # Create a new entry for a label if there is an unused space
            elif len(self.labels_and_counters) < self.number_of_items_to_estimate_frequency_for - 1:

                self.labels_and_counters[stream_character] = 1

            # Decrement all counters since the label was not found and all counters are in use
            else:

                labels_to_remove = []

                for label in self.labels_and_counters:

                    self.labels_and_counters[label] -= 1

                    # Remove dictionary entry if counter is zero
                    if self.labels_and_counters[label] == 0:
                        labels_to_remove.append(label)

                # Remove entries for labels that have reached zero count
                for label in labels_to_remove:
                    del self.labels_and_counters[label]

    # Return the characters along with the counter
    def get_character_count_estimates(self):

        labels = list()
        label_counts = list()

        for label in self.labels_and_counters:
            labels.append(label)
            label_counts.append(self.labels_and_counters[label])

        return labels, label_counts
  
    
class TestMisraGriesFrequentItems(unittest.TestCase):

    def test_for_s1_and_s2(self):

        for file_name in [MisraGriesFrequentItems.S1_FILE_NAME, MisraGriesFrequentItems.S2_FILE_NAME]:
            misra_gries_frequent_items \
                = MisraGriesFrequentItems(file_name, MisraGriesFrequentItems.NUMBER_OF_ITEMS_TO_ESTIMATE_FREQUENCY_FOR)
            misra_gries_frequent_items.estimate_character_counts()
            print("Estimated char counts in file " + file_name)
            print(misra_gries_frequent_items.get_character_count_estimates())

"""
Self test
"""
if __name__ == "__main__":
    unittest.main()
