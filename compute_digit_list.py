# Note for first three problems, instead of looping just use list(range)!

# For primes -- Use sieve of Eratosethenes (more efficent algorithm):
# Note I referenced w3 as I didn't recall the exact definition.
def generate_primes_list(number):
    upperbound = number + 1 # want to consider number
    non_primes = set() # keep track of all non-primes
    primes = []

    for i in range(2, upperbound):
        if i in non_primes:
            continue

        for j in range(i * 2, upperbound, i): # if a number can be a multiple, its not prime
            non_primes.add(j)

        primes.append(i)

    return primes
