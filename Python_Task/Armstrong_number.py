sayi = input("Enter positive number\n")
a = len(sayi)
liste = []

if sayi.isnumeric() == True:
    for i in sayi:
        liste.append(int(i)**a)

    b = sum(liste)

    if int(sayi) == b:
        print(sayi, "is an Armstrong number")
    else:
        print(sayi, "is not an Armstrong number")
    
else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    







