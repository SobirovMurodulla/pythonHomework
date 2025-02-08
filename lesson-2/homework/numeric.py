#numeric
#1-question
n = float(input())
print(round(n,2))

#2-question
a,b,c = map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>a:
    if b>c:
        print(b)
    else:
        print(c)
else:
    print(c)

#3-question
kilometers = float(input())
meters = kilometers * 1000
centimeters = meters * 100
print("meters: ", meters)
print("centimeters: ", centimeters)

#4-question
num1,num2 = map(int,input().split())
print("Integer division: ", int(num1/num2), " remainder: ", num1 % num2)

#5-question
celcius = float(input())
farenheit = celcius * 1.8 + 32
print("Farenheit: ", farenheit)

#6-question
number1 = int(input())
last_digit = number1%10
print(last_digit)

#7-question
number2 = int(input())
if number2%2==0:
    print("Even")
else:
    print("Odd")
