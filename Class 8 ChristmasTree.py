
from random import randint

width = 25 # Tree width
body_height = 25 # Height without stand
full_height = 31 # Total height

tree = ''
for x in range(1, full_height, 2):
    s = ''
    center = int((width-1)/2)
    padding = center-int((x-1)/2)
    
    print('\n', end='') 
    
    if x == 1 :
        print(' '*padding, end='') 
        print('*', end='') 
    elif x < body_height:   
        print(' '*padding, end='')
        for y in range(0,x):
            b = randint(0, width) # Location to add random decoration 1
            a = randint(0, width) # Add random decoration 2
            c = randint(0, width) # Add random decoration 3
            if y==b:
                print('o', end='') 
            elif y==a:
                print('@', end='') 
            elif y==c:
                print('+', end='') 
            else:
                print('^', end='')  
        
        
    elif x == body_height:
        print(' '*padding, end='') 
        print('#'*width, end='') 
    elif x > body_height and x < full_height:
        print(' '*center, end='') 
        print('II', end='')  
        
print('\n', end='') 
print(('~'*width).center(width))  
print('MERRY CHRISTMAS'.center(width)) 
print('AND'.center(width))
print('HAPPY HOLIDAYS !'.center(width))
print(('~'*width).center(width))  