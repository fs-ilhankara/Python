def fizzbuzz():
    liste = []
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            i = "FizzBuzz"
            liste.append(i)
        elif i%3 ==0:
            i = "Fizz"
            liste.append(i)
        elif i%5 == 0:
            i = "Buzz"
            liste.append(i)
        else:
            liste.append(i)
    print(liste)
fizzbuzz()        
