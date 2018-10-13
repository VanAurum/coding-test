# cli.py
import sys

from subtract_times import subtract_time_ranges

import click



@click.command()
@click.option('--change-input',
              type=click.Choice(['A', 'B','run']),
              help='Enter your own list of time ranges', 
              prompt='Enter the list you would like to \nchange, or enter run to use default lists',
)
def main(change_input):
    A=['9:00-10:00','10:25-15:25']
    B=['9:15-9:45','10:15-14:00']
    if change_input:
        if (change_input=='A'):
            while True:
                A = click.prompt('Please enter new list of time ranges',type=str,default="eg. '10:00-10:30', '11:45-12:00', etc...")
                valid,msg=valid_input(A)
                if (valid):
                    print('List A has been updated with the following entries:')
                    print(msg)
                    break
                print('')
                print(msg)
                print('')
                print('List was not in the right format. Examples are:')
                print("['8:30-10:00', '22:00-22:05', '00:12-00:46']")
                print("['5:00-5:30', '6:00-7:00']")
                print('Input must be a list.')
                print('')    
            main()    
        elif(change_input=='B'):
            B = click.prompt('Please enter new list of time ranges')
            print('List B has been updated with the following entries:')
            for item in B:
                print(item)
            main()    
        elif(change_input=='run'):
            results=subtract_time_ranges(A,B)
            
            print('\nAnswer:')
            for result in results:
                print(result)
            print('')    
            main()
    main()

def valid_input(X):
    if (type(X) is not list and type(X) is not str):
        msg='Time range is not in the correct format'
        return False, msg
    try:
        X=list(X)
    except:
        msg='Unable to convert entry to list.'   
    if (type(X)!=list):
        msg='Input was not a list. Make sure your entries are contained within [] brackets.'
        return False, msg   
    if (len(X)==0):
        msg='An empty list was provided.  Please add at least one time range.'
        return False, msg        
    if (':' not in X):
        msg='Time range was not in the correct format. Make sure times are in the format: "09:00" or "22:30"'
        return False,msg
    if (X.count(':')<2):
        msg='One of the times in the range is missing ":"'
        return False,msg
    if ('-' not in X):
        msg='You are missing a dash in your time range'
        return False,msg        

    return True, X    

                  
if __name__ == "__main__":
    A=['9:00-10:00','10:25-15:25']
    B=['9:15-9:45','10:15-14:00']
    print('\n\n\n\n')
    print (30 * '-')
    print ("   M A I N - M E N U✨")
    print('  By: Kevin Vecmanis')
    print (30 * '-')

    print('Hello League. This is my submission \nfor the coding test. Enjoy!')
    print('')
    print('Default choices, for demonstration \npurposes, are:')
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