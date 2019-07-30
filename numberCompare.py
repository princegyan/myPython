#Finding the Greatest Number of Three Numbers

#Accepting Inputs
firstNum = int(input("Enter First Number "))
secondNum = int(input("Enter First Number "))
thirdNum = int(input("Enter First Number "))

#Checking Conditions
if (firstNum > secondNum) and (firstNum > thirdNum):
    largestNum = firstNum
elif(secondNum > firstNum) and (secondNum > thirdNum):
    largestNum = secondNum
else:
    largestNum = thirdNum

print("The largest number between",firstNum,",",secondNum,"and",thirdNum,"is",largestNum)