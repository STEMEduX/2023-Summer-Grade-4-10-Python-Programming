import random

count = 0

while True:
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    num3 = random.randint(10,99)
    num4 = random.randint(10,99)
    num5 = random.randint(10,99)
    num6 = random.randint(10,99)
    num7 = random.randint(10,99)
    num8 = random.randint(10,99)
    print(num1, " + ",  num2, " =        ", num3, " + ",  num4, " =        ", num5, " + ",  num6, " =        ", num7, " + ",  num8, " =        " )
    ##print(" ")
    count = count + 1
    if count == 25:
        break

print(" ")
print(" ")
print(" ")
print(" ")
count = 0

while True:
  num1 = random.randint(10,99)
  num2 = random.randint(10,99)
  if num2 > num1:
      num = num1
      num1 = num2
      num2 = num
  
  num3 = random.randint(10,99)
  num4 = random.randint(10,99)
  if num4 > num3:
    num = num3
    num3 = num4
    num4 = num
    
  num5 = random.randint(10,99)
  num6 = random.randint(10,99)
  if num6 > num5:
    num = num5
    num5 = num6
    num6 = num
  num7 = random.randint(10,99)
  num8 = random.randint(10,99)
  if num8 > num7:
    num = num7
    num7 = num8
    num8 = num
  print(num1, " - ",  num2, " =        ", num3, " - ",  num4, " =        ", num5, " - ",  num6, " =        ", num7, " - ",  num8, " =        " )
  ##print(" ")
  count = count + 1
  if count == 25:
      break
