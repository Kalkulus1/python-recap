def manipulate_generator(generator, n):
    non_primes = [1]  # Initialize the list with the first non-prime number

    while True:
        is_prime = True
        num = next(generator)  # Get the next number from the generator

        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break

        if not is_prime:
            non_primes.append(num)
        
        if len(non_primes) == n:
            break

    return non_primes

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
