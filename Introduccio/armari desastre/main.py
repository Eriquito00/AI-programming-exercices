from classes.Cloth import Cloth

armari = []
for i in range(50):
    armari.append(Cloth())

print("Armari de roba:")
for c in armari:
    print(c.toString())