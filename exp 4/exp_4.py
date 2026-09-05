import time
import sys

# Increase the limit for integer string conversion to print massive numbers
sys.set_int_max_str_digits(500000)

class FibonacciCalculator:
    """A class containing efficient methods to compute the nth Fibonacci number."""
    
    @staticmethod
    def iterative_method(n):
        """
        Computes the nth Fibonacci number using a space-optimized iterative approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        if n == 0:
            return 0
            
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def fast_doubling_method(n):
        """
        Computes the nth Fibonacci number using the Fast Doubling algorithm.
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to the recursion stack
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")

        # Helper function that returns a tuple containing (F(k), F(k+1))
        def _fib(k):
            if k == 0:
                return (0, 1)
            
            # Recursively calculate F(k//2) and F(k//2 + 1)
            a, b = _fib(k >> 1)  # Bitwise right shift is equivalent to k // 2
            
            # Apply Fast Doubling formulas:
            # F(2k) = F(k) * [2 * F(k+1) - F(k)]
            # F(2k+1) = F(k)^2 + F(k+1)^2
            c = a * (2 * b - a)
            d = a * a + b * b
            
            if k & 1:  # Check if k is odd using bitwise AND
                return (d, c + d)
            else:
                return (c, d)

        # We only need F(n), which is the first element of the returned tuple
        return _fib(n)[0]


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    n = 100_000  # A moderately large number to demonstrate efficiency

    print(f"--- Calculating the {n}th Fibonacci Number ---")

    # 1. Test Iterative Method O(n)
    start_time = time.time()
    result_iterative = FibonacciCalculator.iterative_method(n)
    end_time = time.time()
    iterative_duration = end_time - start_time
    print(f"\n[Iterative Method] Time taken: {iterative_duration:.5f} seconds")

    # 2. Test Fast Doubling Method O(log n)
    start_time = time.time()
    result_fast = FibonacciCalculator.fast_doubling_method(n)
    end_time = time.time()
    fast_duration = end_time - start_time
    print(f"[Fast Doubling Method] Time taken: {fast_duration:.5f} seconds")

    # Verify both methods produced the exact same result
    assert result_iterative == result_fast, "Results do not match!"
    print("\nVerification: Both methods yielded the same result.")
    
    # Optional: Print the length of the resulting number (it will be huge!)
    num_digits = len(str(result_fast))
    print(f"The resulting Fibonacci number contains {num_digits} digits.")