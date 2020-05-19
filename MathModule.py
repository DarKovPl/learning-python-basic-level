import math

f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(math.ceil(f_smaller), math.ceil(f_bigger),
      '\n')  # zwraca najmniejszą liczbe całkowitą która jest większa od przekazanego argumetu

print(math.floor(f_smaller), math.floor(f_bigger),
      '\n')  # zwraca największą liczbe całkowitą która jest mniejsza od przekazanego argumentu

print(math.ceil(-f_smaller), math.ceil(-f_bigger), '\n')

print(math.floor(-f_smaller), math.floor(-f_bigger), '\n')

print(pow(2, 8), pow(9, 0.5), '\n')  # Potęgi, Pierwastki

print(math.sqrt(16), '\n')  # Pierwiastek kwadratowy

print(math.pi, math.e, '\n')  # Zmienne stałe

print(math.sin(math.pi / 2), math.cos(math.pi / 4))
print('-----------------------------------------------------')

# Laboratory

degree = 360
print((math.pi / 180) * degree, '\n')

degree = 45
print((math.pi / 180) * degree, '\n')

print(math.radians(360), '\n')
print(math.radians(45))
print('-----------------------------------------------------')

small_pizza_r = 22
small_pizza_price = 11.50
big_pizza_r = 27
big_pizza_price = 15.60
family_pizza_r = 38
family_pizza_price = 22.00

small_pizza_area = round(math.pi * small_pizza_r ** 2 / 10000, 6)
big_pizza_area = round(math.pi * big_pizza_r ** 2 / 10000, 6)
family_pizza_area = round(math.pi * family_pizza_r ** 2 / 10000, 6)

print("Small pizza surface area: {0:.6f}m\u00b2".format(small_pizza_area))
print("Big pizza area surface: {0:.6f}m\u00b2".format(big_pizza_area))
print("Family pizza area surface: {0:.6f}m\u00b2".format(family_pizza_area))
print("Price for 1m\u00b2 of small pizza: " + str(round(small_pizza_price/small_pizza_area, 6)))
print("Price for 1m\u00b2 of big pizza: " + str(round(big_pizza_price/big_pizza_area, 6)))
print("Price for 1m\u00b2 of family pizza: " + str(round(family_pizza_price/family_pizza_area, 6)))
