#The interval Newton method finds all roots in a given interval.

from interval import interval

#Solving x - x^3 in the interval [-10,10]
print(interval[-10, 10].newton(lambda x: x - x**3, lambda x: 1 - 3*x**2))

#Solving x^2 - 2 in the interval [-2, 2]
print(interval[-2, 2].newton(lambda x: x**2 - 2, lambda x: 2*x))

#Solving x^6 - x^5 + x^3 + x^2 - 3 in the interval [-3, 5]
print(interval[-3, 5].newton(lambda x: x**6 - x**5 + x**3 + x**2 - 3, lambda x: 6*x**5 - 5*x**4 + 3*x**2 + 2*x))
