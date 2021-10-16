"""
24. Napisati metod int najveciNeparniDjelilac(int n) koji vraća najveći neparni
pozitivni djelilac broja n. 
"""

n = int(input('Unesite broj: '))

def najveciNeparniDjelilac(n):
    D = 1
    djelilac = 0

    while n >= D:
        if n%D == 0 and D%2 != 0:
            djelilac = D
            D = D +1
        else:
            D = D + 1
    return djelilac

print(najveciNeparniDjelilac(n))