#Simple Calculator

#addition function
def addition(x, y):
    return x + y

#subtraction function
def subtraction(x, y):
    return x - y

#division function
def division(x, y):
    return x / y

#multiplication function
def multiplication(x, y):
    return x * y

#Entering first and second numbers respectively
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter choice(1/2/3/4):")


if choice == '1':
   print(num1,"+",num2,"=", addition(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtraction(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", division(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", multiplication(num1,num2))
else:
   print("Input is Invalid")