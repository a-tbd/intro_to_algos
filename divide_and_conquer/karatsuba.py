'''
Coursera Intro to Algorithms

Divide and Conquer: Karatsuba multiplication

Useage: karatsuba.py number1 number2
len(number1) == len(number2)

Examples:
24 32 ==> 768

timeit for a = 24, b = 32
karatsuba = 0.0031259059906
grad_school = 0.00705313682556
'''
import sys
import timeit
import pdb

def grade_school(a, b):
    n = len(a)
    a = [int(m)*10**(n-i-1) for i, m in enumerate(a)]
    b = [int(m)*10**(n-i-1) for i, m in enumerate(b)]
    sums = [[i*j for j in b] for i in a]
    return sum([sum(i) for i in sums])


def karatsuba(a, b):
    n = len(a)
    # pdb.set_trace()
    x_h = a[:n/2]
    x_l = a[n/2:]
    y_h = b[:n/2]
    y_l = b[n/2:]
    if n == 2:
        return multiply(int(x_h), int(x_l), int(y_h), int(y_l))
    else:
        return (karatsuba(x_h, y_h)*10**n + 
               (karatsuba(x_h, y_l) + karatsuba(y_h, x_l))*10**(n/2) + 
               karatsuba(x_l, y_l))

def karatsuba2(a, b):
    n = len(a)
    # pdb.set_trace()
    digits = {'x_h': a[:n/2],
              'x_l': a[n/2:],
              'y_h': b[:n/2],
              'y_l': b[n/2:]}
    if n == 2:
        digits_int = {d: map(int, digits[d][0]) for d in digits}
        print digits_int
        return (digits['x_h']*digits['y_h']*100 + 
               (digits['x_h']*digits['y_l'] + 
                digits['y_h']*digits['x_l'])*10 + 
                digits['x_l']*digits['y_l'])
    else:
        return (karatsuba(digits['x_h'], digits['y_h'])*10**n + 
               (karatsuba(digits['x_h'], digits['y_l']) + 
                karatsuba(digits['y_h'], digits['x_l']))*10**(n/2) + 
               karatsuba(digits['x_l'], digits['y_l']))

def multiply(x_h, x_l, y_h, y_l):
    return x_h*y_h*100 + (x_h*y_l + y_h*x_l)*10 + x_l*y_l

def main(argv):
    try:
        a, b = argv
    except:
        print 'useage: python karatsuba.py number1 number2 '
        sys.exit(2)
	
    print karatsuba(a, b)
    # rint grade_school(a, b)
    # print karatsuba2(a, b)

if __name__ == "__main__":
    main(sys.argv[1:])