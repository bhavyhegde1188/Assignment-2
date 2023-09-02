Factorial and bionomial coefficient
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
if n == 0 or n == 1:
return 1
else:
return n * fact(n-1)
n_minus_r = fact(n-r)
r_fact = fact(r)
print("Factorial: ", fact(n))
def fact(n):
print("Binomial Co-efficient: ", fact(n)/(n_minus_r*r_fact))
Enter the value of n: 5
Enter the value of r: 3
Factorial: 120
Binomial Co-efficient: 10.0
