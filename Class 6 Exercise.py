## Quiz Problem 1
rows = eval(input('Please input how many rows: '))
cols = eval(input('Please input how many cols: '))

print('')
for i in range(rows):
    print('*'* cols)

# Quiz Problem 2
rows = eval(input('Please input how many rows: '))
cols = eval(input('Please input how many cols: '))

print('')
for i in range(rows):
#    if i in (0, rows - 1, 6):  
    if i == 0 or i == rows - 1:
        print('*'* cols)
    elif i == 5:
        print('*' * cols)
    elif i == 7:
        print('*' + ' ' * 13 + '*' * 3 + ' ' * 12 + '*')
    else:
        print('*' + (' ') * (cols - 2) + '*')

# Quiz Problem 3
for i in range(100, 0, -2):
    print(i, end=' ')
