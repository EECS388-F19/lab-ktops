# Using python, make your script print:
import random

# Your name
print('Kelsey Toporski')

# Two random numbers between 0-100
oop = []
for i in range(2):
    a = random.randint(0, 101)
    oop.append(a)
    print(str(a))

# The sum of the two numbers, starting with "Sum = "
print('Sum = ' + str(sum(oop)))

# The average of the two numbers, starting with "Average = "
print('Average = ' + str((sum(oop)/len(oop))))
