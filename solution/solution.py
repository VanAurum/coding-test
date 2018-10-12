#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:51:01 2018

@author: Kevin Vecmanis
"""
import unittest
from helpers import convert_time_range_to_integers,\
                    clean_time_range_string,\
                    generate_sets_from_tuple_ranges,\
                    subtract_sets,\
                    determine_split_indices,\
                    split_list_on_index,\
                    split_results_on_split_indices,\
                    convert_integer_to_string_time,\
                    convert_time_lists_to_time_string

def subtract_time_ranges(A,B):
    '''Parameters:
    Accepts two lists, A and B, as arguments.  Each list contains time ranges 
    in string 24-hour time format. eg. ['9:00-10:00', 14:20-15:20'].
       
    As boundaries for this function, time resolution can be down to 
    the minute.  
    '''
    #Create a list of tuples with integer representations of the time (in minutes)
    integer_times_A = [convert_time_range_to_integers(time_range) for time_range in A]
    print('Integer Times A:') 
    print(integer_times_A)
    integer_times_B = [convert_time_range_to_integers(time_range) for time_range in B]
    print('Integer Times B:') 
    print(integer_times_B)
    #generate a list of sets
    sets_A = generate_sets_from_tuple_ranges(integer_times_A)
    sets_B = generate_sets_from_tuple_ranges(integer_times_B)
    print('Sets A:')
    print(sets_A)
    print('Sets B:')
    print(sets_B)
    #subtract each timerange in B from each time range in A
    results=subtract_sets(sets_A,sets_B)
    print('Results from subtract_sets')
    print(results)
    #get indices to split results on
    split_indices = determine_split_indices(results)
    print('Results from determine_split_indices')
    print(split_indices)
    final_list = split_results_on_split_indices(results, split_indices)
    print('Final List:')
    print(final_list)
    solution = convert_time_lists_to_time_string(final_list)
    print(solution)         
    return solution

A=['9:00-10:00', '10:00-10:30']
B=['9:15-10:15']
solution=subtract_time_ranges(A,B)
    
