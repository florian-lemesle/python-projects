import random


# je crée une table de traduction des lettres avec accent car dans le pendu les accents ne comptent pas

def translate_char(mot):
    result = ""

    translation_table = {

        'à': 'a',
        'è': 'e',
        'é': 'e',
        'ê': 'e',
        'ë': 'e',
        'ç': 'c',
        'ï': 'i',
        'î': 'i',
        'ô': 'o',
        'ù': 'u',
        'û': 'u',
        'ü': 'u',
    }
    for x in mot:
        if x in translation_table.keys():
            result = result + translation_table[x]
        else:
            result = result + x

    return result


# je choisis un mot au hasard dans mon dictionnaire et je crée les variables dont j'ai besoin

solution = random.choice(open('dico_france.txt').read().split()).strip()
niveau = input("Choisissez le niveau de difficulté: ")
lettres_trouvees = ""
listlettres = []
affichage = ""

# je crée plusieurs niveau de difficulté

while not (niveau == "facile" or niveau == "moyen" or niveau == "difficile"):
    print("Veuillez choisir entre facile, moyen et difficile.")
    niveau = input("Choisissez le niveau de difficulté: ")

if niveau == "facile":
    vie = 10
elif niveau == "moyen":
    vie = 7
elif niveau == "difficile":
    vie = 4

print(" ")
print("-------------------")
print("  Tu as", vie, "vies!")
print("-------------------")

# mon affichage affichera un nombre d'underscore de la longeur du mot à trouver

for l in translate_char(solution):
    affichage += "_ "

# tant que le joueur possède une ou plusieurs vie, il peut continuer à jouer
# quand le joueur entre une lettre je l'ajoute à la liste des lettres essayées

while vie > 0:

    print(" ")
    print("Mot à trouver:", affichage)
    if niveau != "difficile":
        print("Lettres choisies: ", listlettres)
        print(" ")
        lettre = input("Quelle lettre proposes tu? ")
        listlettres.append(lettre)
    else:
        print(" ")
        lettre = input("Quelle lettre proposes tu? ")
        listlettres.append(lettre)

    # tant que le joueur ne rentre pas qu'une seule lettre je crée une boucle d'erreur

    while len(lettre) > 1:
        print(" ")
        print("Tu ne dois entrer qu'une seule lettre! ")
        print(" ")
        lettre = input("Quelle lettre proposes tu? ")
        listlettres.append(lettre)

    # si le joueur trouve une lettre

    if lettre in translate_char(solution):
        lettres_trouvees += lettre
        print(" ")
        print("Correct. Il te reste", vie, "vies.")

    # si il se trompe je lui retire un point de vie

    else:
        vie -= 1
        print(" ")
        print("Essai encore! Il te reste", vie, "vies.")

        if vie == 0:
            print(" ")
            print("Dommage... Tu as perdu.")
            print(" ")
            print("Le mot à trouver était", solution)
            print(" ")
            x = input("Appuyez sur entrée pour quitter.")

            if not x:
                print(" ")
                print("Au revoir.")
                exit()

    # je met à jour l'affichage du mot à trouver

    affichage = ""
    for x in translate_char(solution):
        if x in lettres_trouvees:
            affichage += x
            affichage += " "
        else:
            affichage += "_ "

    # si l'affichage du mot à trouver ne contient plus de lettre à trouver, le joueur à gagné

    if "_ " not in affichage:
        print(" ")
        print("Bien joué! Tu as gagné!")
        print(" ")
        print("Le mot à trouver était", solution)
        print(" ")
        x = input("Appuyez sur entrée pour quitter.")

        if not x:
            print(" ")
            print("Au revoir.")
            exit()
        break
