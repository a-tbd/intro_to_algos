'''
Coursera Intro to Algorithms

Divide and Conquer: Karatsuba multiplication
'''
import sys
import pdb

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
    		   (karatsuba(x_h, y_l) + karatsuba(y_h, x_l)) + 
    		   karatsuba(x_l, y_l))

def multiply(x_h, x_l, y_h, y_l):
    return (x_h*y_h*100) + ((x_h*y_l) +(y_h*x_l))*10 + (x_l*y_l)

def main(argv):
	try:
		a, b = argv
	except:
		print 'useage: python karatsuba.py number1 number2'
		sys.exit(2)
	
	print karatsuba(a, b)

if __name__ == "__main__":
    main(sys.argv[1:])