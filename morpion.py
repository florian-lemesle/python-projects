import csv

do = input("Bonjour, souhaites tu jouer (->jouer) ou voir les scores (->scores)? ")

while not (do == "jouer" or do == "scores"):
    do = input("Bonjour, souhaites tu jouer (->jouer) ou voir les scores (->scores)? ")

if do == "jouer":

    joueur1 = input("Joueur 1 Croix: ")
    joueur2 = input("Joueur 2 Rond: ")

    while joueur1 == joueur2:
        print("Joueur 2 doit être différent de Joueur 1")
        joueur2 = input("Joueur 2 Rond: ")

win = 0
tour = joueur1

ligne0 = ["-", "-", "-"]
ligne1 = ["-", "-", "-"]
ligne2 = ["-", "-", "-"]

while win == 0:

    for i in range(3):
        print(ligne0[i], " ", end='')
    print(" ")
    for i in range(3):
        print(ligne1[i], " ", end='')
    print(" ")
    for i in range(3):
        print(ligne2[i], " ", end='')
    print(" ")

    print("C'est au tour de ", tour)

    ligne = input("Entrez le numero de la ligne : ")
    colonne = int(input("Entrez le numero de la colonne : "))

    if tour == joueur1:

        if ligne == "0":
            ligne0[colonne] = "X"
        elif ligne == "1":
            ligne1[colonne] = "X"
        elif ligne == "2":
            ligne2[colonne] = "X"

    if tour == joueur2:

        if ligne == "0":
            ligne0[colonne] = "O"
        elif ligne == "1":
            ligne1[colonne] = "O"
        elif ligne == "2":
            ligne2[colonne] = "O"

    if (ligne0[0] == ligne0[1]) and (ligne0[1] == ligne0[2]) and (ligne0[0] != "-"):
        win = 1
    if (ligne1[0] == ligne1[1]) and (ligne1[1] == ligne1[1]) and (ligne1[0] != "-"):
        win = 1
    if (ligne2[0] == ligne2[1]) and (ligne2[1] == ligne2[2]) and (ligne2[0] != "-"):
        win = 1
    if (ligne0[0] == ligne1[0]) and (ligne1[0] == ligne2[0]) and (ligne0[0] != "-"):
        win = 1
    if (ligne0[1] == ligne1[1]) and (ligne1[1] == ligne2[1]) and (ligne0[1] != "-"):
        win = 1
    if (ligne0[2] == ligne1[2]) and (ligne1[2] == ligne2[2]) and (ligne0[2] != "-"):
        win = 1
    if (ligne0[0] == ligne1[1]) and (ligne1[1] == ligne2[2]) and (ligne0[0] != "-"):
        win = 1
    if (ligne0[2] == ligne1[1]) and (ligne1[1] == ligne2[0]) and (ligne0[2] != "-"):
        win = 1
    if (ligne0[0] != "-") and (ligne0[0] != "-") and (ligne0[1] != "-") and (ligne0[2] != "-") and (
            ligne1[0] != "-") and (ligne1[1] != "-") and (ligne2[0] != "-") and (ligne2[1] != "-") and (
            ligne2[2] != "-"):
        win = 2

    if win == 1:
        print(" ")
        print("Le joueur", tour, "à gagné!")
        print(" ")
        x = input("Appuyez sur entrée pour quitter.")

        if not x:
            print(" ")
            print("Au revoir.")
            exit()

    if win == 2:
        print("Match nul! Aucun joueurs n'a gagné!")
        print(" ")
        x = input("Appuyez sur entrée pour quitter.")

        if not x:
            print(" ")
            print("Au revoir.")
            exit()

    if tour == joueur1:
        tour = joueur2

    else:
        tour = joueur1

# if do == "scores": (censé afficher le contenu du ficher score.txt

""""

Pour la seconde partie de l'exercice j'ai testé deux "début" de solutions mais je n'ai pas eu le temps d'aller plus 
loin... 

il faut trouver un moyen pour lire le texte, qu'on va découper en mots et le mettre en mémoire sous forme de liste, 
vérifier que la variable qui contient le nom du joueur n'est pas égale à l'un des objets de la liste, sinon on l'ajoute
 et crée son score, sinon on doit sortir le char score associé au joueur, le transformer en int, 
l'incrémenter de 1, le repasser en char et écraser l'ancien score avec le score mis à jour. Ce n'est pas vraiment ce 
que j'ai fais avec mes début de solution mais passons. 


        with open('score.csv', 'a', newline='') as csvfile:
            titres = ['Joueur', 'Score']
            writer = csv.DictWriter(csvfile, fieldnames=titres)

            if tour in titres[0]:
                writer.writeheader()
                titres[1] += 1
            else:
                writer.writeheader()
                writer.writerow({'Joueur': tour, 'Score': 1})
"""

"""

      with open("score.txt", 'r') as file:
           data = [line.strip() for line in file]
      for line in data:
           list1 = (line.split())
      print(list1)
      for x in list1:
      if list1[1] == joueur:
            print("Joueur", joueur, "est déjà dans le fichier!")
            break
"""
