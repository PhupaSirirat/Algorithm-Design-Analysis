import time

def is_prime(n):
    operations = 0
    if n < 2:
        operations += 1
        return False, operations
    for i in range(2, int(n**0.5) + 1):
        operations += 1
        if n % i == 0:
            operations += 1
            return False, operations
    operations += 1
    return True, operations

def prime_factorization(n):
    factors = []
    operations = 0
    for i in range(2, n + 1):
        is_prime_result, prime_ops = is_prime(i)
        operations += prime_ops
        operations += 1
        if is_prime_result:
            while n % i == 0:
                operations += 1
                factors.append(i)
                n //= i
            if n == 1:
                break
    return factors, operations

def FindGCD1(m, n):
    total_operations = 0
    
    print("Step 1: Prime factorization of m")
    m_factors, m_ops = prime_factorization(m)
    print(f"Factors of {m}: {m_factors}")
    print(f"Operations for Step 1: {m_ops}")
    total_operations += m_ops
    
    print("\nStep 2: Prime factorization of n")
    n_factors, n_ops = prime_factorization(n)
    print(f"Factors of {n}: {n_factors}")
    print(f"Operations for Step 2: {n_ops}")
    total_operations += n_ops
    
    print("\nStep 3: Find common prime factors")
    common_factors = []
    m_index = n_index = 0
    step3_ops = 0
    while m_index < len(m_factors) and n_index < len(n_factors):
        step3_ops += 1
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
    
    print("\nStep 4: Compute GCD")
    gcd = 1
    step4_ops = 0
    for factor in common_factors:
        gcd *= factor
        step4_ops += 1
    print(f"GCD({m}, {n}) = {gcd}")
    print(f"Operations for Step 4: {step4_ops}")
    total_operations += step4_ops
    
    print(f"\nTotal operations: {total_operations}")
    return gcd, total_operations

# Example usage
m, n = 48, 18
start_time = time.time()
result, totalOperations = FindGCD1(m, n)
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")