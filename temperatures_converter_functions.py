def celcius_to_fahrenheit(celcius):
    return celcius * (9/5) + 32

def celcius_to_kevin(celcius):
    return celcius + 273.15

def fahrenheit_to_celcius(fahrenheit):
    return fahrenheit - 32 * (5/9)

def fahrenheit_to_kevin(fahrenheit):
    return (fahrenheit - 32 * (5/9)) + 273,15

def kevin_to_celcius(kevin):
    return kevin - 273.15

def kevin_to_fahrenheit(kevin):
    return ((kevin - 273.15) * (9/5)) + 32