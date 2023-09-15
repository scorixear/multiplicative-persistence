import functools
from typing import Callable
import time
import sys
curr_max = 0
curr_max_num = 0

timit_counter = 0

@functools.lru_cache(maxsize=None)
def persistence(n: int, base: int = 10):
    """Returns the multiplicative persistence of n in base b."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if base < 2:
        raise ValueError("base must be greater than 1")
    if n < base:
        return 0
    prod = product(n, base)
    #print(prod)
    return 1 + persistence(product(n, base), base)

@functools.lru_cache(maxsize=None)
def product(n: int, base: int):
    """Returns the product of the digits of n in base b."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if base < 2:
        raise ValueError("base must be greater than 1")
    if n < base:
        return n
    return (n % base) * product(n // base, base)

def input_read():
    while True:
        n = int(input("Enter a number:\n"))
        print(f"persistence({n}) = {persistence(n)}")

def print_timit(time: float):
    global timit_counter
    timit_counter += 1
    if timit_counter % 10000 == 0:
        timit_counter = 0
        sys.stdout.write(f"\rTime: {time/1000}ms 10000 calls")
        sys.stdout.flush()

def perm_with_rep(nums: list[int], size: int, curr_perm: list[int], execute: Callable[[int], int]):
    if size == 0:
        global curr_max
        global curr_max_num
        number = int("".join([str(i) for i in curr_perm]))
        #print(number)
        timit_start = time.perf_counter_ns()
        pers = execute(number)
        timit_end = time.perf_counter_ns()
        print_timit(timit_end - timit_start)
        if pers > curr_max:
            curr_max = pers
            curr_max_num = number
            print(f"New max: {curr_max} for {curr_max_num}\n")
        return
    for i in nums:
        curr_perm.append(i)
        perm_with_rep(nums, size - 1, curr_perm, execute)
        curr_perm.pop()
def calc_size(size=233):
    # small at beginning
    # only 2,3,4 max 1
    # never 5

    # 7,8 and 9 fillup
    # start space at 233
    small = [2, 3, 4, None]
    fillup = [7, 8, 9]
    curr = []
    for i in small:
        if i is not None:
            curr.append(i)
        perm_with_rep(fillup, size - len(curr), curr, persistence)

def main():
    calc_size(233)
    #input_read()
        
            
if __name__ == "__main__":
    main()