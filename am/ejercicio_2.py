#!/usr/bin/env python3

#  Ejercicio 2
#
#  Eres un importante repartidor de una empresa de paqueteria, tu mision es escoger de una lista de N paquetes disponibles 2 paquetes de los cuales la suma de sus dimensiones en centimetros cubicos deje solo 90 centimetros cubicos de espacio en tu camioneta, el interior de tu camioneta es de 250 centimetros cubicos. En el caso de que encuentres varios pares de paquetes que cumplan con la condicion de los 90 centimetros cubicos tendras que escoger el par de paquetes que tenga el paquete de mayor dimension.
#
#
# ( 50 40 20 230 90 30 10 50 70 80 110 )
#
# Tamano de la camioneta - suma de pares = 90cm3 de espacio
#
# Par 1 = 250 - ( 90 + 70 ) = 90
# Par 2 = 250 - ( 110 + 50 ) = 90 <<<--- Este es el par seleccionado

packages = [50, 40, 20, 230, 90, 30, 10, 50, 70, 80, 110]
good_pairs = []

# Look for good pairs
for i, package in enumerate(packages):
    pair_size = 160
    desire_size = pair_size - package
    if desire_size in packages[i:]:
        good_pairs.append((package, desire_size))
print(good_pairs)

# Get the bigger package
#bigger_package = 0
#for pair in good_pairs:
#    max_package = max(pair)
#    if bigger_package < max_package:
#        bigger_package = max_package
bigger_package = max(map(max, good_pairs))

# Look for the pair with the bigger package
for pair in good_pairs:
    if bigger_package in pair:
        print(pair)
        break
