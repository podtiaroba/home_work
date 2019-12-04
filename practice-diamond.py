#https://github.com/Bandydan/php/blob/master/06_Practice_practice_practice.md
#Задача 2. Бриллиант

x = int (input("Insert the number: "))
s = []
for i in range (1, 1 + x):
  if i%2!=0:
    print(' '.join('*'*i).rjust(x*2))