"""
1. Napisati kod koji za date katete a i b (a<b) pravouglog trougla računa površinu i
zapreminu tijela koje se dobija rotacijom trougla oko manje katete.
"""
import math

a = float(input('Unesite duzinu prve katete: '))
b = float(input('Unesite duzinu druge katete: '))
c = math.sqrt(a*a + b*b)
povrsina_kupe_rotacijom_oko_a = a*a*3.14 + a*c*3.14
povrsina_kupe_rotacijom_oko_b = b*b*3.14 + b*c*3.14

def kupa_dobijena_rotacijom_trougla():
    if a > b:   
        return povrsina_kupe_rotacijom_oko_b
    else:
        return povrsina_kupe_rotacijom_oko_a

print(kupa_dobijena_rotacijom_trougla())