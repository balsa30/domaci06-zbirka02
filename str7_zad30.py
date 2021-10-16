"""
30. Prirodan broj n je Armstrongov ako je jednak zbiru kubova svojih cifara. Npr. 371 je
Armstrongov, jer je 3^3+7^3+1^3=371. Napisati metod boolean isArmstrong(int n) koji
za dati broj n provjerava da li je Armstrongov, i ako jeste, vraća true, a ako nije, vraća
false. 
"""

n = int(input('Provjerite Armstrongov broj: '))

def Armstrongov_broj(n):
    k = n
    zbir = 0
    while k > 0:
        zbir = zbir + (k%10)*(k%10)*(k%10)
        k = k // 10

    if n == zbir:
        return True
    else:
        return False

print(Armstrongov_broj(n))