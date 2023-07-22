rows = 5
cols = 23

for i in range(rows):
    print('*' + ('*' if i in (0, rows - 1) else ' ') * (cols - 2) + '*')
