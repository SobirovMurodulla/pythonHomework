#1-question
username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Username and password are not empty.")
else:
    print("Username and password are empty.")

#2-question
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#3-question
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("Number is not positive and even.")

#4-question
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    print("All three numbers are different.")
else:
    print("Not all three numbers are different.")

#5-question
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) == len(string2):
    print("Both are equal.")
else:
    print("The strings are not equal.")

#6-question
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#7-question
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if (num1 + num2) > 50:
    print("The sum is greater than 50.")
else:
    print("The sum is not greater than 50.")

#8-question
num = int(input("Enter a number: "))

if 10 <= num <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20 (inclusive).")