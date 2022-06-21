#products of digits of a number

n = int(input("Enter the number of digits:"))

p = 1

while n:
    
    p = p * (n % 10)
    
    n = n // 10
    
    print(f'The product of the digits of a number: {p}')
