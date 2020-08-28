# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 2
# count = 1
#
# #check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


Fibanachi = [1, 1]


def fibonacci(n):
    if n < 1:
        print("Incorrect input")
    elif n <= len(Fibanachi):
        return Fibanachi[n - 1]
    else:
        fib_num = fibonacci(n - 1) + fibonacci(n - 2)
        Fibanachi.append(fib_num)
        return fib_num


print(fibonacci(8))

