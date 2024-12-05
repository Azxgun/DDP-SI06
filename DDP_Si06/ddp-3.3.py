def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = celcius_ke_fahrenheit(celcius)
print('Suhu dalam Fahrenheit: ' ,fahrenheit)