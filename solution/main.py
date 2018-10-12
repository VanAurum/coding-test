#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:51:01 2018

@author: Kevin Vecmanis
"""
import unittest

def subtract_time_ranges(A,B):
    '''Parameters:
    Accepts two lists, A and B, as arguments.  Each list contains time ranges 
    in string 24-hour time format. eg. ['9:00-10:00', 14:20-15:20'].
       
    As boundaries for this function, time resolution can be down to 
    the minute.  
    '''
    #Create a list of tuples with integer representations of the time (in minutes)
    integer_times_A=[convert_time_range_to_integers(time_range) for time_range in A]
    integer_times_B=[convert_time_range_to_integers(time_range) for time_range in B]
    #generate a list of sets
    sets_A=generate_sets_from_tuple_ranges(integer_times_A)
    sets_B=generate_sets_from_tuple_ranges(integer_times_B)
    #subtract each timerange in B from each time range in A
    results=subtract_sets(sets_A,sets_B)
    #get indices to split results on
    split_indices=determine_split_indices(results)

               
    return
    
