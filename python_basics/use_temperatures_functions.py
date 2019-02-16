from temperatures_converter_functions import *
import sys


temperatura = float((input("\nDigite uma temperatura: ")))

print("\nTemperatura convertida para Fahrenheit: {}\n".format(celcius_to_fahrenheit(temperatura)))

temperatures = [10, -20, 100]

for temperature in temperatures:
    print(celcius_to_fahrenheit(temperature))