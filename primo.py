number = int(input("Enter a number: "))

if number > 1:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    print(f"{number} is a prime number." if is_prime else f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")
