def computeGCD():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
             
    if num1 > num2: 
        small = num2 
    else: 
        small = num1 
    for i in range(1, small+1): 
        if((num1 % i == 0) and (num2 % i == 0)): 
            gcd = i     
    return gcd

print(computeGCD())
