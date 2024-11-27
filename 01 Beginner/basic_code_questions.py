"""
Comprehensive Python Coding Problem Statements Collection

This script contains solutions to various coding problems, demonstrating
different programming concepts and problem-solving techniques.
"""

import math
from typing import List, Optional
import itertools

class CodingProblems:
    @staticmethod
    def reverse_string(s: str) -> str:
        """
        Reverse a given string
        
        Methods:
        1. Slicing
        2. Reverse iteration
        3. Recursive approach
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Method 1: Slicing
        print("Reverse String Methods:")
        print("1. Slicing:", s[::-1])
        
        # Method 2: Reverse iteration
        reversed_str = ''.join(reversed(s))
        print("2. Reversed iteration:", reversed_str)
        
        # Method 3: Recursive approach
        def recursive_reverse(string):
            if len(string) <= 1:
                return string
            return recursive_reverse(string[1:]) + string[0]
        
        print("3. Recursive:", recursive_reverse(s))
        
        return s[::-1]

    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Check if a number is prime
        
        Prime number criteria:
        1. Greater than 1
        2. No divisors other than 1 and itself
        
        Methods:
        1. Basic iteration
        2. Optimized square root method
        
        Time Complexity: O(√n)
        Space Complexity: O(1)
        """
        print("\nPrime Number Check:")
        
        # Method 1: Basic iteration
        def basic_prime_check(num):
            if num <= 1:
                return False
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        
        # Method 2: Optimized square root method
        def optimized_prime_check(num):
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        print("Basic Method:", basic_prime_check(n))
        print("Optimized Method:", optimized_prime_check(n))
        
        return optimized_prime_check(n)

    @staticmethod
    def fibonacci_series(n: int) -> List[int]:
        """
        Generate Fibonacci Series
        
        Methods:
        1. Iterative approach
        2. Recursive approach
        3. Generator approach
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        print("\nFibonacci Series Generation:")
        
        # Method 1: Iterative
        def iterative_fibonacci(limit):
            fib = [0, 1]
            while len(fib) < limit:
                fib.append(fib[-1] + fib[-2])
            return fib[:limit]
        
        # Method 2: Recursive
        def recursive_fibonacci(limit):
            def fib(n):
                if n <= 1:
                    return n
                return fib(n-1) + fib(n-2)
            
            return [fib(i) for i in range(limit)]
        
        # Method 3: Generator
        def generator_fibonacci(limit):
            a, b = 0, 1
            for _ in range(limit):
                yield a
                a, b = b, a + b
        
        print("Iterative:", iterative_fibonacci(n))
        print("Recursive:", recursive_fibonacci(n))
        print("Generator:", list(itertools.islice(generator_fibonacci(n), n)))
        
        return iterative_fibonacci(n)

    @staticmethod
    def factorial(n: int) -> int:
        """
        Calculate Factorial of a Number
        
        Methods:
        1. Iterative approach
        2. Recursive approach
        3. Functional approach
        
        Time Complexity: O(n)
        Space Complexity: O(1) for iterative, O(n) for recursive
        """
        print("\nFactorial Calculation:")
        
        # Method 1: Iterative
        def iterative_factorial(num):
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result
        
        # Method 2: Recursive
        def recursive_factorial(num):
            if num <= 1:
                return 1
            return num * recursive_factorial(num - 1)
        
        # Method 3: Functional (using reduce)
        def functional_factorial(num):
            return math.prod(range(1, num + 1))
        
        print("Iterative:", iterative_factorial(n))
        print("Recursive:", recursive_factorial(n))
        print("Functional:", functional_factorial(n))
        
        return iterative_factorial(n)

    @staticmethod
    def print_patterns(rows: int) -> None:
        """
        Print Various Number and Star Patterns
        
        Patterns:
        1. Right-angled triangle
        2. Pyramid
        3. Inverted pyramid
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        print("\nPattern Printing:")
        
        # Right-angled Triangle
        print("Right-angled Triangle:")
        for i in range(1, rows + 1):
            print('* ' * i)
        
        # Pyramid Pattern
        print("\nPyramid Pattern:")
        for i in range(1, rows + 1):
            print(' ' * (rows - i) + '* ' * i)
        
        # Inverted Pyramid
        print("\nInverted Pyramid:")
        for i in range(rows, 0, -1):
            print(' ' * (rows - i) + '* ' * i)

    @staticmethod
    def even_odd_operations(numbers: List[int]) -> None:
        """
        Even and Odd Number Operations
        
        Operations:
        1. Separate even and odd numbers
        2. Count even and odd numbers
        3. Sum of even and odd numbers
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        print("\nEven and Odd Number Operations:")
        
        # Separate even and odd numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]
        
        print("Original Numbers:", numbers)
        print("Even Numbers:", even_numbers)
        print("Odd Numbers:", odd_numbers)
        
        # Count even and odd numbers
        print("Even Count:", len(even_numbers))
        print("Odd Count:", len(odd_numbers))
        
        # Sum of even and odd numbers
        print("Sum of Even Numbers:", sum(even_numbers))
        print("Sum of Odd Numbers:", sum(odd_numbers))

    @staticmethod
    def palindrome_check(s: str) -> bool:
        """
        Check if a string is a palindrome
        
        Methods:
        1. Simple reversal
        2. Two-pointer approach
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        print("\nPalindrome Check:")
        
        # Method 1: Simple reversal
        def simple_palindrome(string):
            return string == string[::-1]
        
        # Method 2: Two-pointer approach
        def two_pointer_palindrome(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        print("Simple Method:", simple_palindrome(s))
        print("Two-Pointer Method:", two_pointer_palindrome(s))
        
        return simple_palindrome(s)

def main():
    """
    Demonstration of various coding problem solutions
    """
    problems = CodingProblems()
    
    print("=" * 50)
    print("CODING PROBLEM DEMONSTRATIONS")
    print("=" * 50)
    
    # Reverse String
    problems.reverse_string("Hello, World!")
    
    # Prime Number
    problems.is_prime(17)
    
    # Fibonacci Series
    problems.fibonacci_series(10)
    
    # Factorial
    problems.factorial(5)
    
    # Pattern Printing
    problems.print_patterns(5)
    
    # Even Odd Operations
    problems.even_odd_operations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Palindrome Check
    problems.palindrome_check("racecar")

if __name__ == "__main__":
    main()
