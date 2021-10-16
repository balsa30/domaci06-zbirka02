"""
2. Napisati metod int zbirIzIntervala(int a, int b) koji vraća zbir svih cijelih
brojeva iz intervala [a,b]
"""

a = int(input('Unesite prvi interval: '))
b = int(input('Unesite drugi interval: '))

def zbirIzIntervala(a, b):
    zbir = 0
    while a <= b:
        zbir = zbir + a
        a = a + 1
    else:
        return zbir

print(zbirIzIntervala(a, b))