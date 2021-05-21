def letters_count():
    a = input("bir string giriniz.")
    b = {}
    for i in a:
        b[i] = a.count(i)
    return print(b)

letters_count()