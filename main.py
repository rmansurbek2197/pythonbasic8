def sonlar_yigindisi(sonlar):
    yigindisi = 0
    for son in sonlar:
        yigindisi += son
    return yigindisi

sonlar = [1, 2, 3, 4, 5]
print(sonlar_yigindisi(sonlar))