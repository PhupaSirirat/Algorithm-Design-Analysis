'''
FindGCD1(m,n) 
Step 1  Find the prime factorization of m 
Step 2  Find the prime factorization of n 
Step 3  Find all the common prime factors 
Step 4  Compute the product of all the common prime factors and return it as gcd(m,n) 
Where the prime factorization technique is implemented by a Naive solution.
'''
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
    
    m_factors, m_ops = prime_factorization(m)
    total_operations += m_ops
    
    n_factors, n_ops = prime_factorization(n)
    total_operations += n_ops
    
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
    total_operations += step3_ops
    
    gcd = 1
    step4_ops = 0
    for factor in common_factors:
        gcd *= factor
        step4_ops += 1
    total_operations += step4_ops
    
    return gcd, total_operations

def run_test_case(m, n):
    start_time = time.time()
    result, totalOperations = FindGCD1(m, n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"GCD({m}, {n}) = {result}")
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Total operations: {totalOperations}")
    print("-" * 40)

# Test cases
test_cases = [
    (48, 18),
    (1000, 750),
    (123456, 78910),
    (9876543, 6543210),
]

for i, (m, n) in enumerate(test_cases, 1):
    print(f"Test Case {i}:")
    run_test_case(m, n)