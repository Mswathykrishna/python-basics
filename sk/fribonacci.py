def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
    terms=int(input("Enter the number of terms:"))
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i))
