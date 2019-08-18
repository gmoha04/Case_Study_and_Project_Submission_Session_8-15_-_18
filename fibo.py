def fib2(nterms):
    n1 = 0
    n2 = 1
    
    # check if the number  is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(*[0,1,1])
    else:
       print("Fibonacci sequence upto",nterms,":")
       while n1 <= nterms:
           print(n1,end=' , ')
           nth = n1 + n2
       # update values
           n1 = n2
           n2 = nth