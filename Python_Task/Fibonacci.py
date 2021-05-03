def fibonacci(n):
    liste = []
    a, b, c = 0, 0, 1
    #x = int(input("Enter last number : \n"))    
    while c<= n: # x (if we ask user input)
        liste.append(c)        
        a = b
        b = c
        c = a + b
    print(liste)

fibonacci(55)


