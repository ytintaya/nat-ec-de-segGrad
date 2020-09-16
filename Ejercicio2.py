a = int(input("ingrese a: \n"))
b = int(input("ingrese b: \n"))
c = int(input("ingrese c: \n"))
d = b**2 - 4*a*c
if d > 0:
    print("raices reales")
elif d == 0:
    print("raices reales e iguales")
elif d < 0:
    print("raices complejas")