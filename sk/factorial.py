def factorial(n):
    ifn== 0:
        return 1
    else:
        return n*factorial(n-1)
    num=int(input("Enter a number:"))
    print("factorial:",factorial(num))
