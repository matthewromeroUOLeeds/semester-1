
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    '''
    if number == -1:
        return None
    else:
        print(number) 
        countdown(number-1) 

countdown(10)