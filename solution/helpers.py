#solutions/helpers.py
'''
About helper.py:
This module contains all the testable support functions used in the main solution in solution/main.py
'''

def convert_time_range_to_integers(time_range):
    '''Convert time range string to tuple of minute-based integers.
    Accepts a string-based time range as an argument. The purpose 
    of this function is to convert the string-based time into an integer 
    representing the time in minutes. For example, when provided 
    with '9:00-10:00' as a range, it will return (540,600).
    '''
    #Clean time_range
    time_range=clean_time_range_string(time_range)
    #Split into two times   
    x,y=time_range.split('-')
    #Split first time into hours and minutes
    x1,x2=x.split(':')
    #Split second time into hours and minutes
    y1,y2=y.split(':')
    #Cast all sub components as integer
    x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)
    #Calculate time in minutes for start time.
    start=(x1*60)+x2
    #Calculate time in minutes for end time.
    end=(y1*60)+y2
    return (start,end)

def clean_time_range_string(time_range):
    '''Handle common non-standard entries for time-range. Input should be in 24-hour time 
    but I'm trying to make the function as robust as possible to input variation.
    Removes 'am', 'AM', 'pm', 'PM'. 
    Removes whitespace contained within the string. 
    '''
    #Remove all whitespace
    time_range=time_range.replace(' ','')
    #Remove extraneous entries in the time range
    time_range=time_range.replace('am','')
    time_range=time_range.replace('AM','')
    time_range=time_range.replace('pm','')
    time_range=time_range.replace('PM','')
    return time_range

def generate_sets_from_tuple_ranges(list_of_ranges):
    '''Converts a list of integer time ranges to sequential sets.
    For example: 
    [(5,10), (6,8)] will become:
    [{5,6,7,8,9,10}, {6,7,8}]
    This conversion is done so that set and intersection theory can be applied to efficiently
    and robustly subtract times. For tuple ranges with zero distance, like (2,2), nothing is returned 
    because this is assumed to represent a timeslot with zero time.
    '''
    #convert list of ranges to list of lists
    x=[list(range(a[0],a[1]+1)) for a in list_of_ranges if (a[0]!=a[1])]
    #convert list of lists to list of sets
    x=[set(a) for a in x]
    return x

def subtract_sets(A,B):
    '''Accepts two lists of sets representing time ranges and iteratively subtracts the intersection of each set.
    If the resulting set is {}, it is not included in the results list.
    '''
    results=[]
    for set_a in A:
        temp=set_a
        for set_b in B:
            temp=temp-set_a.intersection(set_b)    
        results.append(temp)
    #convert list of sets to list of lists if set is not empty.
    results=[list(a) for a in results if len(a)!=0]
    return results

def determine_split_indices(results):
    '''Checks if there are 'time gaps' in the result list and returns the indices of the discontinuity.
    For example: 
        if a list is [[1,2,3,6,7,8,9]], the output will be [2].
        if a list is [[1,2,4,5,7,8]], the output will be [1,3].
        if a list is [[1,2,4,5], [6,7,9,10]], the output will be [[1],[1]]

    The purpose of this is to capture the edge case where a slice of time inside a range is subtracted.
    '''
    split_indices=[]
    for list_ in results:
        sublist=[]
        for i in range(0,len(list_)-1):
            if ((list_[i+1]-list_[i])!=1):
                sublist.append(i)
        split_indices.append(sublist)
    return split_indices            

       
