year = int(input("Lütfen 4 haneli olacak şekilde yıl giriniz: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} artık yıldır.")
    else:
        print(f"{year} artık yıl değildir. ")
elif year % 4 == 0:
    print(f"{year} artık yıldır")
else:
    print(f"{year} artık yıl değildir. ")
