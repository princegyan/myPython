import math

def summation():
    i = 1
    answer = 0
    for i in range (i,100):
        a = math.sqrt((i*math.pi)/100)
        b = (i*math.pi)/100
        s = a*math.sin(b)
        answer = answer + s
        print(answer)

summation()
