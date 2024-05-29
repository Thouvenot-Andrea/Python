# afficher hello World
print("hello World")

# affectation
a = 5
b = 7
c = a + b
print("a vaut ", a)
print("b vaut ", b)

# pour ne pas aller à la ligne après le prochain print mettre end=""
print("a vaut", a, end=";")
print(" b vaut", b, end=";")
print(" c vaut", c, )

# suite arithmétique
range(10)
print(range(10))
# convertir le résultat en liste
# list(range(10))
print(list(range(10)))
# le 1er chiffre c'est le chiffre de départ,
# le 2eme chiffre c'est le chiffre arriver -1,
# le 3eme chiffre c'est le chiffre du nombre d'écart des chiffre que s'affiche
range(5, 10)
range(-50, -45)
print(list(range(5, 10)))
print(list(range(-50, -45)))
print(list(range(-5, 45, 5)))
# renvoie le nombre d'élément fonction 'len'
a = list(range(7, 10))
print(a)
print(len(a))

# instruction avec if
x = 4
if x > 0:
    print(x, "est positif")
else:
    print(x, "est négatif ou nul")

# instruction avec for
for i in [0, 1, 2]:
    print("valeur :", i)
print("Fin")
# fait la même chose que au dessus
for i in range(3):
    print("i a pour valeur :", i)

d = ["Marc", "est ", "jeune"]
for i in range(len(d)):
    print("i vaut", i, "et d[i] vaut", d[i])

# transformation d'une boucle for en une boucle while
i = 0
while i < 3:
    print("i a pour valeur :", i)
    i += 1

# break pour sortir d'une boucle et passer a l'instruction suivante
# continue permet de passer prématurément au tour de boucle suivant

# permet de savoir le type d'une donnée ou le type de la valeur d'une variable
type(a)
print(type(a))


# fonction sans paramètre
def compteur3():
    i = 0
    while i < 3:
        print(i)
        i += 1


print("bonjour")
compteur3()
print("")


# fonction avec un paramètre


def compteur(stop):
    i = 0
    while i < stop:
        print(i)
        i = i + 1


a = 3
compteur(a)
print()


# fonction avec plusieurs paramètre
def compteur_complet(start, stop, step):
    i = start
    while i < stop:
        print(i)
        i = i + step


compteur_complet(1, 7, 2)
