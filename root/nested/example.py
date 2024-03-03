'''
Created on Feb 29, 2024

@author: mguer
'''
#string example
name = "John"

#Integer example

age = 25

# float example

height = 1.75

#boolean example

is_student = True

#print variable names
print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Is student? ", is_student)

# List example
fruits = ["apple", "banana", "cherry"]
print("List Example: ", fruits)

# Tuple example
coordinates = (3, 7)
print("Tuple Example: ", coordinates)

# Dictionary example
person = {"name": "Alice", "age": 25, "is_student": True}
print("Dictionary Example: ", person)

# Arithmetic operators
num1 = 10
num2 = 3
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
mod_result = num1 % num2
exp_result = num1 ** num2
print("Addition:", add_result) 
print("Subtraction:", sub_result)
print("Multiplication:", mul_result) 
print("Division:", div_result) 
print("Modulus:", mod_result) 
print("Exponentiation:", exp_result)

#Comparison operators
age = 25
is_adult = age >= 18
is_teenager = age >= 13 and age < 18
print("Is adult?", is_adult)
print("Is teenager?", is_teenager)

# Conditional statement example
def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 21:
        print("You are an adult, but ya can't drink yet")
    else:
        print("You are a legal adult")

check_age(20)    

def greet():
    print("Hellow World!")

# call the function to execute
greet()
