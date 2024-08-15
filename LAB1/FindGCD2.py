import time

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    operations = 0
    
    for i in range(2, int(n**0.5) + 1):
        operations += 1  # Comparison in for loop
        if primes[i]:
            for j in range(i*i, n + 1, i):
                operations += 1  # Assignment in inner loop
                primes[j] = False
    
    return primes, operations

def prime_factorization(n, primes):
    factors = []
    operations = 0
    for i in range(2, n + 1):
        operations += 1  # Comparison in for loop
        if primes[i]:
            while n % i == 0:
                operations += 2  # Modulo operation and comparison
                factors.append(i)
                n //= i
        if n == 1:
            break
    return factors, operations

def FindGCD2(m, n):
    total_operations = 0
    
    # Generate primes up to max(m, n)
    max_num = max(m, n)
    primes, sieve_ops = sieve_of_eratosthenes(max_num)
    total_operations += sieve_ops
    print(f"Sieve operations: {sieve_ops}")
    
    # Step 1: Find the prime factorization of m
    print("Step 1: Prime factorization of m")
    m_factors, m_ops = prime_factorization(m, primes)
    print(f"Factors of {m}: {m_factors}")
    print(f"Operations for Step 1: {m_ops}")
    total_operations += m_ops
    
    # Step 2: Find the prime factorization of n
    print("\nStep 2: Prime factorization of n")
    n_factors, n_ops = prime_factorization(n, primes)
    print(f"Factors of {n}: {n_factors}")
    print(f"Operations for Step 2: {n_ops}")
    total_operations += n_ops
    
    # Step 3: Find all the common prime factors
    print("\nStep 3: Find common prime factors")
    common_factors = []
    m_index = n_index = 0
    step3_ops = 0
    while m_index < len(m_factors) and n_index < len(n_factors):
        step3_ops += 1  # Comparison
        if m_factors[m_index] == n_factors[n_index]:
            common_factors.append(m_factors[m_index])
            m_index += 1
            n_index += 1
        elif m_factors[m_index] < n_factors[n_index]:
            m_index += 1
        else:
            n_index += 1
    print(f"Common factors: {common_factors}")
    print(f"Operations for Step 3: {step3_ops}")
    total_operations += step3_ops
    
    # Step 4: Compute the product of all the common prime factors
    print("\nStep 4: Compute GCD")
    gcd = 1
    step4_ops = 0
    for factor in common_factors:
        gcd *= factor
        step4_ops += 1  # Multiplication
    print(f"GCD({m}, {n}) = {gcd}")
    print(f"Operations for Step 4: {step4_ops}")
    total_operations += step4_ops
    
    print(f"\nTotal operations: {total_operations}")
    return gcd, total_operations

# Example usage
m, n = 48, 18
start_time = time.time()
result, totalOperations = FindGCD2(m, n)
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
