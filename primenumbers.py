# Python program to display all the prime numbers within an interval

# Prime Numbers in an Interval

startNum = int(input("Enter starting Number in range: "))
endNum = int(input("Enter ending Number in range: "))

print("Prime numbers between",startNum,"and",endNum,"are:")

for num in range(startNum,endNum + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)