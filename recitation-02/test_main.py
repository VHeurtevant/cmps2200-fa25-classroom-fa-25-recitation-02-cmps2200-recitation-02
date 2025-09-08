from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(18,2,2) == 84 
	assert simple_work_calc(36,3,6) == 63
	assert simple_work_calc(13,5,2) == 243

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(20,4,2,lambda n: 5) == 681
	assert work_calc(15,2,3,lambda n: n*n) == 279
	assert work_calc(5,1,2,lambda n: n*n*n) == 134

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	work_fn1= lambda n: 1
	work_fn2 = lambda n :math.log(n,2)
	work_fn3 = lambda n: n
	res = compare_work(work_fn1, work_fn2,work_fn3,sizes=[10, 20, 50, 100, 1000, 5000, 10000])

	print(res)

	
def test_compare_span():
	span_fn1= lambda n: 1
	span_fn2 = lambda n : math.log(n,2)
	span_fn3 = lambda n : n 

	res = compare_work(span_fn1,span_fn2,span_fn3,sizes=[10, 20, 50, 100, 1000, 5000, 10000])
	print(res)	
