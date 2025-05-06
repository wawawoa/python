# Tel het aantal klinkers in een woord
woord = input("Voer een woord in: ")
klinkers = "aeiou"
aantal_klinkers = 0
for letter in woord:
    if letter in klinkers:
        aantal_klinkers = aantal_klinkers + 1
print("Aantal klinkers:", aantal_klinkers)

# wat wordt er geprint als ik als ik de tekst
# aantal invoer?
# inderdaad invoer>
# a invoer>
# 111 invoer>
# <niets> invoer (gelijk op de ENTER toets druk)?