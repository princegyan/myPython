#Addition

print("Enter First Number")
firstnum = input()
print("Enter Second Number")
secondnum = input()
firstAnswer = firstnum + secondnum
print('='*15)
print("The sum of {0} and {1} is {2}".format(firstnum,  secondnum,  firstAnswer)) #uses variables as strings thus operating them using string concatenation
print('*'*15)
answer = int(firstnum) + int(secondnum) #Correct Answer
print("The sum of {0} and {1} is {2}".format(firstnum,  secondnum,  answer))