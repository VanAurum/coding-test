# solution/cli.py

#python standard module imports
import sys

#local module imports
from subtract_times import subtract_time_ranges
from helpers import clean_time_range_string

#3rd party module imports
import click


A=['9:00-10:00','10:25-15:25']
B=['9:15-9:45','10:15-14:00']
@click.command()
@click.option('--change-input',
              type=click.Choice(['A', 'B','run','quit']),
              help='Enter your own list of time ranges', 
              prompt='Enter the list you would like to \nchange, or enter "run" to use default lists',
)
def main(change_input):
    global A
    global B
    if change_input:
        if (change_input.upper()=='A'):
            while True:
                print('')
                A = click.prompt('Please enter a new list of time ranges. Seperate by a comma if you wish to enter\nmore than one ',type=str,default='eg. 10:00-10:30, 11:45-12:00, etc...')
                print('')
                valid,msg=valid_input(A)
                if (valid):
                    print('List A now contains the following time ranges:')
                    for entry in msg:
                        print(entry)
                    print('')
                    A=msg    
                    break
                print('')
                print(msg)
                print('')
                print('List was not in the right format. Examples are:')
                print('8:30-10:00, 22:00-22:05, 00:12-00:46')
                print('5:00-5:30, 6:00-7:00')
                print('')    
            main()    
        elif(change_input.upper()=='B'):
            while True:
                print('')
                B = click.prompt('Please enter a new list of time ranges. Seperate by a comma if you wish to enter\nmore than one ',type=str,default='eg. 10:00-10:30, 11:45-12:00, etc...')
                print('')
                valid,msg=valid_input(B)
                if (valid):
                    print('List B now contains the following time ranges:')
                    for entry in msg:
                        print(entry)
                    print('')
                    B=msg    
                    break
                print('')
                print(msg)
                print('')
                print('List was not in the right format. Examples are:')
                print("8:30-10:00, 22:00-22:05, 00:12-00:46")
                print('5:00-5:30, 6:00-7:00')
                print('')    
            main()    
        elif(change_input.lower()=='run'):
            try:
                results=subtract_time_ranges(A,B)
            except:
                print('Whoops, an error occurred subtracting these times. Please try new times.')  
                main()            
            print('\nAnswer:')
            for result in results:
                print(result)
            print('')    
            main()
        elif(change_input.lower()=='quit'):
            sys.exit()
            return   
    main()

def valid_input(X):
    list_=[]
    X.replace('[','')
    X.replace(']','')
    X=clean_time_range_string(X)
    if (len(X)==0):
        msg='An empty list was provided.  Please add at least one time range.'
        return False, msg        
    if (':' not in X):
        msg='Time range was not in the correct format. Make sure times are in the format: "09:00" or "22:30"'
        return False,msg
    if (X.count(':')<2):
        msg='One of the times in the range is missing a colon (":")'
        return False,msg
    if ('-' not in X):
        msg='You are missing a dash in your time range'
        return False,msg   
    if (',' in X):
        new=X.split(',')
        for item in new:
            list_.append(item)
    else:
        list_.append(X)
    return True, list_    

                  

A=['9:00-10:00','10:25-15:25']
B=['9:15-9:45','10:15-14:00']
print('\n\n\n\n')
print (30 * '-')
print ("   M A I N - M E N U")
print('  By: Kevin Vecmanis')
print (30 * '-')

print('Hello League. This is my submission \nfor the coding test. Enjoy!')
print('')
print('Default choices for lists A and B are shown below:')
print('')
print('List A:')
for entry in A:
    print(entry)
print('')
print('List B:') 
for entry in B:
    print(entry)
print('')
print (30 * '-') 
main()