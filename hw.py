#Q1.
p = 50

if p > 75:
    grade = "O"
elif 60 < p <= 75:
    grade = "A"
elif 50 < p <= 60:
    grade = "B"
elif 35 < p <= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
#Q2.
n = 7

if n % 2 == 0 and n % 3 != 0:
    print("Divisible by 2, not divisible by 3")
elif n % 3 == 0 and n % 2 != 0:
    print("Divisible by 3, not divisible by 2")
elif n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by 2 and 3")






#1.	
for num in range(21, 81, 2):
              print(num)

#2.	
numbers = []
i in range(1, 21):numbers.append(i)
print(numbers)
numbers = []
#3.	    
for i in range(20, 0, -1):
    numbers.append(i)
    print(numbers)
#4.
cubes = []
                    
for num in range(21, 41, 2):
        	cube = num ** 3
cubes.append(cube)
print(cubes)
#5.	
names = ['a', 'b', 'c', 'd', 'e']
ages = [20, 21, 23, 25, 24]
for i in range(len(names)):
             print(f"My name is {names[i]}, my age is {ages[i]}")

#1.	
my_list = [1, 2, 3, 4, 5]
if len(my_list) >= 2:
     my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)






#2.	
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num = 6
print(f"The factorial of {num} is {factorial(num)}")

#3.	
input_string = "Hello, World!"
string_length = len(input_string)
print(f"The length of the string is: {string_length}")
