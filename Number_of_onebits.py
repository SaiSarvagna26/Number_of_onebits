def Number_of_onebits(number):
    count=0
    while number>0:
        if number&1:
            count+=1
        number>>=1
    return count

number=int(input())
print(Number_of_onebits(number))