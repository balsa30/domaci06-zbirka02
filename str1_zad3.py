"""
3. Napisati kod koji za datu osnovicu a i krak b jednakokrakog trougla računa površinu i
zapreminu tijela koje se dobija rotacijom trougla oko visine spuštene na osnovicu.
"""

import math

a = float(input('Unesite duzinu prve katete: '))
b = float(input('Unesite duzinu druge katete: '))
h = math.sqrt(b*b - (a/2)*(a/2))

povrsina = (a/2)*(a/2)*3.14 + (a/2)*b*3.14
print(povrsina)