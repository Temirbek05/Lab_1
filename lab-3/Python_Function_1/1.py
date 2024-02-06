
# A recipe you are reading states how many grams you need
# for the ingredient. Unfortunately, your store only sells items in ounces.
# Create a function to convert grams to ounces. ounces = 28.3495231 * grams

grams = float(input("Enter the weight in grams: "))
def converter(grams):
    return 28.3495231 * grams
ounces = converter(grams)
print("Weight in ounces:", ounces)