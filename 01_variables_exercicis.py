###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

encaminador = "router"
ubicació = "planta alta, escriptori"
numero_ports = 6
ences = True

print(f"L'encaminador s'enomena {encaminador}, es troba ubicat en {ubicació}, compte amb {numero_ports} ports i es {ences} que esta encès")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

GB_pla = 34
GB_consumits = 8
total = GB_pla - GB_consumits

print(f"Et queden {total}GB")


GB_consumits = GB_consumits + 7
total = GB_pla - GB_consumits

print(f"Et queden {total}GB")
