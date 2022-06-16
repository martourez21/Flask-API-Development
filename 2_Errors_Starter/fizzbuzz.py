
numbers = [1,2,15,3,4,5,6,7,8,9,10]

for n in numbers:
    if n%3==0 and n%5==0:
        print("FIZZ " + str(n))
    elif n%5==0:
        print("BUZZ " +str(n))
    elif n%3==0:
        print("FIZZ BUZZ")
    else:
        print(n)
