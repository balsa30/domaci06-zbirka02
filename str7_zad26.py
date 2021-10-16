"""
26. Napisati metod boolean jeProst(int n) koji za dati broj n provjerava da li je prost, i
ako jeste, vraća true, a ako nije, vraća false. 
"""

n = int(input('Unesite prost broj: '))

def jeProst(n):
    djelilac = 2
    indikator = 1

    while djelilac < n:
        if n%djelilac == 0:
            indikator = 0
            djelilac = djelilac + 1
        else:
            djelilac = djelilac + 1
    else:
        if indikator == 1:
            return True
        else:
            return False

print(jeProst(n))