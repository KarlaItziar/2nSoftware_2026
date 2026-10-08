###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

paquets = input("Quants paquets ha rebut el encaminador? ")

enter = int(paquets)
suma = paquets + 1200

print("En total hi ha {suma} paquets en el magatzem.")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

velocitat = input("Quina és la velocitat de la connexió en Mbps? ")
decimal = float(velocitat)
mbps = decimal / 8
print(f"La velocitat equivalent en MB/s és de {mbps:.2f} MB/s")