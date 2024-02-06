# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)


Fahrenheit = float(input("Enter the weight in grams: "))

def Calculate(Fahrenheit):
    return (5 / 9) * (Fahrenheit - 32)

centigrade = Calculate(Fahrenheit)
print("Weight in ounces:", centigrade)