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