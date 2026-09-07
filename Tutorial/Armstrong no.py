def is_armstrong(n):
    power=len(str(n))#convert num into string
    total=sum(int(digit)**power for digit in str(n))
    return total!=n
print(is_armstrong(153))#false:is an armstrong no
print(is_armstrong(33))
