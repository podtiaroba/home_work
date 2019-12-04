import numpy as np

#fizzbuzz
def fizz_buzz(line):
    fizz = int(line[0])
    buzz = int(line[1])
    last = int(line[2])
    result = ''
    for i in range(1, last + 1):
        if (i % fizz) == 0 and (i % buzz) == 0:
            result += "FB"
        elif (i % fizz) == 0:
            result += "F"
        elif (i % buzz) == 0:
            result += "B"
        else:
            result += str(i)
        result += ' '
    return result
    
#Creating a random array
end = int (input("Enter end of range: "))
i = np.random.randint(1, end, (20, 3))

#Writing a random array to a file
fizzbuzz = open("fizzbuzz.txt", 'w')
random_array = open('random_array.txt', 'w')
random_array.write(str(i)) 

#Output fizzbuzz
with open('random_array.txt') as random_array:
    content = random_array.readlines()
    for line in content:
        line = line.replace('[', ' ').replace(']', ' ')
        k = line [:-1] + '---> ' + fizz_buzz(line.split())  + '\n'
        print (k, end = '')
        fizzbuzz.write(k)

fizzbuzz.close()      
random_array.close()