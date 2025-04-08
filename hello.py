def factoeial(n)
	if n == 0;
		return 1
	else :
		return n * factoriel(n - 1)

number = 5
result = factorial(number)
print(f"the factorial of (number) is (result)."
