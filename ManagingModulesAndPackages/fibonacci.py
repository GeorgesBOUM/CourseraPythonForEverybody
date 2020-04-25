#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:39:22 2020

@author: gregoire
"""

# Fibonacci numbers module


def write_fibo(n):
    """# write Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def return_fibo(n):
    """# return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    num = 5
    write_fibo(num)
    print(return_fibo(num))
