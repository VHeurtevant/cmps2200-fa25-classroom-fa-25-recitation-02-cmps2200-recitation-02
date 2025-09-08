"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n<=1:
		return 1
	else:
		return a*simple_work_calc(n//b,a,b)+n

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n<=1:
		return 1
	else:
		return a*work_calc(n//b,a,b,f)+ f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n<=1:
		return 1
	else:
		return span_calc(n//b,1,b,f)+ f(n)



def compare_work(work_fn1, work_fn2, work_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		
		work1 = work_calc(n,1,2,work_fn1)
		work2 = work_calc(n,4,2,work_fn2)
		work3 = work_calc(n,8,2,work_fn3)
		result.append((
			n,
			work1,
			work2,
			work3
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2','W_3'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2,span_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		span1 = span_calc(n,1,2,span_fn1)
		span2 = span_calc(n,1,2,span_fn2)
		span3 = span_calc(n,1,2,span_fn3)
		# compute W(n) using current a, b, f
		result.append((
			n,
			span1,
			span2,
			span3
			))
	return result
	


if __name__ == '__main__':
    
	span_fn1= lambda n: 1
	span_fn2 = lambda n : int(math.log(n,2))
	span_fn3 = lambda n: n
	res = compare_span(span_fn1, span_fn2,span_fn3,sizes=[10, 20, 50, 100, 1000, 5000, 10000])
	print_results(res)
	