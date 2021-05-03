number = int(input("Enter number : "))

liste_asal = []
if number > 1:
    for i in range(1,number + 1):
        if number % i == 0:
            liste_asal.append(i)
    if len(liste_asal)>2 :
        print(number,"is not a prime number")
    else:
        print(number, "is a prime number")
else:
    print(number,"is not a prime number")

