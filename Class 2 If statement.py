x = 34 - 23 # A comment.
y = "Hello" # Another one.
z = 3.45
if z == 3.45 or y == "Hello":
    x = x + 1
    y = y + " World" # String concat.
print (x)
print (y)


def ReadLine():
    sentence = input("Please enter a sentence: ")
    return sentence

while True:
    line = ReadLine()
    if len(line) == 0:
        break
    print(line)

for letter in 'Hello, world':    
    print (letter)
for i in range(2,10,2):
    print (i)
