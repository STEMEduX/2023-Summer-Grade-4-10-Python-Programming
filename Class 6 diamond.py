

# Quiz Problem 2
rows = eval(input('Please input how many rows: '))
cols = eval(input('Please input how many cols: '))

print('')
for i in range(rows):
    if i in (0, rows - 1):  
        print('*'* cols)  
    elif i == 3 or i == 7:
        print('*' + (' ') * 14 + '*'  +(' ') * 13+ '*')
    elif i == 4 or i == 6:
        print('*' + (' ') * 13 + '***'  +(' ') * 12+ '*')
    elif i == 5:
        print('*' + (' ') * 12 + '*' * 5 +(' ') * 11+ '*')
    else:
        print('*' + (' ') * (cols - 2) + '*')

