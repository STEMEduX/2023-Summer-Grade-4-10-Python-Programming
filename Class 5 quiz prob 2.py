rows = eval(input('Please input how many rows: '))
cols = eval(input('Please input how many cols: '))

print('')
for i in range(rows):
    if i in (0, rows - 1):  
        print('*'* cols)
    else:
        print('*' + (' ') * (cols - 2) + '*')
