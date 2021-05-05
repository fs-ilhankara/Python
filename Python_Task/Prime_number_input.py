n = int(input("Enter a number :\n"))
count = 0
liste = []
for i in range(2, n+1) :
    for j in range(1, i+1):
        if i % j == 0 :
            count += 1
    if count < 3:
        liste.append(i)
    count = 0
print(liste)    