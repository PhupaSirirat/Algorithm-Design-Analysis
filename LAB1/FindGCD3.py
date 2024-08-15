import time

def FindGCD3(m, n, depth=0):
    operations = 1  # Count the comparison operation

    # For debugging and visualization of recursion
    indent = "  " * depth
    print(f"{indent}Computing GCD({m}, {n})")

    if n == 0:
        print(f"{indent}n = 0, returning {m}")
        return m, operations
    elif m == 0:
        print(f"{indent}m = 0, returning {n}")
        return n, operations
    elif m == n:
        print(f"{indent}m = n, returning {m}")
        return m, operations
    elif m > n:
        operations += 1  # Count the modulo operation
        remainder = m % n
        print(f"{indent}m > n, recursive call: GCD({n}, {remainder})")
        result, sub_operations = FindGCD3(n, remainder, depth + 1)
        return result, operations + sub_operations
    else:  # m < n
        operations += 1  # Count the modulo operation
        remainder = n % m
        print(f"{indent}m < n, recursive call: GCD({m}, {remainder})")
        result, sub_operations = FindGCD3(m, remainder, depth + 1)
        return result, operations + sub_operations

def run_FindGCD3(m, n):
    print(f"Finding GCD of {m} and {n}")
    start_time = time.time()
    result, total_operations = FindGCD3(m, n)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"\nGCD({m}, {n}) = {result}")
    print(f"Total operations: {total_operations}")
    print(f"Execution time: {execution_time:.6f} seconds")
    return result, total_operations, execution_time

# Example usage
m, n = 48, 18
result, total_operations, execution_time = run_FindGCD3(m, n)