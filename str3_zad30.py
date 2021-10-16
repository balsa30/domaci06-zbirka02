"""
30. Dva automobila se kreću po kružnoj staži dužine L u suprotnim smjerovima. Polaze iz iste
tačke i kreću se stalnim brzinama v1 i v2. Na kom rastojanju će se naći automobili u
trenutku T. Ulaz: U jednom redu zadaju se 4 cijela broja L, v1, v2, T, razdvojeni blankom
(1 ≤ L, v1, v2, T ≤ 100). Izlaz: Štampati jedan cio broj – rastojanje automobila u trenutku T
"""

L = int(input('Duzina staze u km: '))
v1 = int(input('Brzina automobila 1 u km/h: '))
v2 = int(input('Brzina automobila 2 u km/h: '))
T = int(input('Vrijeme u h: '))

L1 = v1 * T
L2 = v2 * T
rastojanje = L - L1 - L2

if L >= 1 and T <= 100:
    print('Rastojanje izmedju automobila u km: ', rastojanje)
else:
    print('Duzina staze je mora biti vea od 1 km i vrijeme manje od 100h.')