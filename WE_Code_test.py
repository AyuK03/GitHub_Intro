import math

def check(num):

    s1 = len(str(num))
    cop = num
    sum1 =0

    while(num!=0):

        sum1+=math.pow(int(num%10),s1)

        num= int(num//10)

    print(sum1)

    if int(sum1)==cop:
        return "Y"
    else:
        return "N"

n = int(input("Enter a num : "))

print(check(n))


