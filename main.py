from functools import reduce

'''
fib(0) = 0
fib(1) = 1
'''

# fibVal(n) -> Single value
fibVal = lambda n : reduce(lambda x,_ : [x[1], x[0]+x[1]], range(n), [0,1])[0]

# fibSeq(n) -> Sequence (up to value 4)
fibSeq = lambda n : [reduce(lambda x,_ : [x[1], x[0]+x[1]], range(num), [0,1] )[0] for num in range(n+1)]

print(fibVal(4))
print(fibSeq(4))