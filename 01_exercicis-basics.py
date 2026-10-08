###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###


print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.\n")

### Completa aquí

print("Karla Suquia Vegué \nHospitalet")


print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.\n")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a),"\n",type(b),"\n",type(c),"\n",type(d),"\n",type(e))


print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
cadena = "12345"
enter = int(cadena)
decimal = float(cadena)

print(cadena,"\n",enter,"\n",decimal)

num = 3.99

print(num,"\n",int(num),"\n") 
## No podrem pasar d'un nombre "dificil" com es un decimal a un "sencill", un enter.


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
nom= "Karla Suquia Vegue"
edat= 18
altura= 1.73

print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {altura} metres")


print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí
from cmath import pi

nombrepi = pi
arrodonit = round(nombrepi)
operacio = arrodonit // 2
print(operacio)


print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
temperatura = input("Introdueix la temperatura en graus Celsius:")
celcius = float(temperatura)
fahrenheit = (celcius * 9/5) + 32

print(f"la temperatura en fahrenheit es de {fahrenheit}F")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
compte = input("Digues el total del compte: ")
propina = input("Quin persentatge de propina vols deixar: ")

total = compte * (propina//100)

print(f"Hauras de deixar {total:.2f}€ de propina")


print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contrasenya = input("Introdueix la teva contrasenya: ")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")
### Completa aquí