from random import*

x = randint(1,12)
ylist = []
z = 0
c = 0

while z<10:
  y = randint(1,12)
  while y in ylist:
    y = randint(1,12)
  ylist.append(y)
  a = int(input("What is "+str(x)+" times "+str(y)+"? "))
  b = x*y
  if a == b:
    c += 1
  z += 1

print("You got",c,"questions right out of 10")
