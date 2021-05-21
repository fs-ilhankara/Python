def letters_count():
    a = input("bir string giriniz.")
    b = {}
    for i in a:
        c = a.count(i)
        b[i] = c
    return print(b)

letters_count()