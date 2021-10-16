"""
7. Napisati metod int zbirDjelilaca(int n) koji vraća zbir pozitivnih djelilaca broja n
manjih od n. 
"""

n = int(input('Unesite broj n: '))

def zbirDjelilaca(n):
    djelilac = 2
    zbir = 1
    while n > djelilac:
        if n % djelilac != 0:
            djelilac = djelilac + 1
        else:
            zbir = zbir + djelilac
            djelilac = djelilac + 1
    else:
        return zbir

print(zbirDjelilaca(n))