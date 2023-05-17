def sortowanie(ttt):
    n = len(ttt)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ttt[j] < ttt[j + 1]: 
                ttt[j], ttt[j + 1] = ttt[j + 1], ttt[j]

odpowiedz = input("Podaj 4 liczby oddzielone spacją\n")
liczby = odpowiedz.split()
sortowanie(liczby)
print(liczby)
