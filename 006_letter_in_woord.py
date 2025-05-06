woord = input("Voer een woord in: ")
letter = input("Voer een letter in om te zoeken: ")
gevonden = False
for char in woord:
    if char == letter:
        gevonden = True
        break
if gevonden:
    print("De letter komt voor in het woord.")
else:
    print("De letter komt niet voor in het woord.")

# wat wordt er geprint als ik
# het woord test invoer en de letter s invoer?
# het woord huiswerk invoer en de letter o invoer?
# het woord huis invoer en de letters uis invoer?
# <niets> invoer (gelijk op de ENTER toets druk) en dan de letter a invoer?
# het woord test invoer en dan <niets> invoer (gelijk op de ENTER toets druk)?