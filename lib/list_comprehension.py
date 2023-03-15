#!/usr/bin/env python3

def return_evens(num_list):
    return [num_list[i] for i in range(len(num_list)) if num_list[i] % 2 == 0 ]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]