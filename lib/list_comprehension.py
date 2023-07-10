#!/usr/bin/env python3
def even_num(even_list, num):
    if (num % 2 == 0):
        even_list.append(num)

def return_evens(num_list):
    even_list = []
    [even_num(even_list, num) for num in num_list]
    return even_list

def make_exclamation(sentence_list):
    return [word + "!" for word in sentence_list]
