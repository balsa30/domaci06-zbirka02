"""
23. Date su dvije promjenljive x i y istog tipa. Napisati kod koji mijenja mjesta vrijednostima u
promjenljivim x i y. Npr. ako je x = 5 i y = 10, poslije izvršavanja koda treba da bude x=10 i
y=5.
"""

x = int(input('Unesite prvi broj x: '))
y = int(input('Unesite drugi broj y: '))

x, y = y, x

print(f'x = {x}', f'y = {y}')