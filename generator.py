import random
import time
file_name = input("What is the name of the file where you want to save generated data?\n")
time.sleep(0.8)
print("OK, we gonna save data in " + file_name + ".txt")
time.sleep(1)
while True :
    check = input("Do you confirm? Please answer by Yes or No\n")
    check = check.lower()
    if check == "yes" : break
    elif check == "no" :
        file_name = input("Quel est le nom du fichier ou vous souhaiter enregistrer les données générées ?\n")
        time.sleep(0.8)
        print("D'accord nous allons enregistrer les données sur le fichier " + file_name + ".txt")
    else :
        print("Veuillez répondre par Oui ou Non!")
        time.sleep(0.8)

time.sleep(1)

what = input("Que soitez-vous générer? Tapez 1 pour des numéros de téléphone et 2 pour des plaques d'immatriculations ?\n")
while True :
    if what == "1" : break
    elif what == "2" : break
    else :
        print("Veuillez répondre par 1 ou 2")
        what = input("Que soitez-vous générer? Tapez 1 pour des numéros de téléphone et 2 pour des plaques d'immatriculations")

if what == "1" :
    what = "numero(s) de telephone"
    print("D'accord nous allons générez des " + what)
    while True:
        nb = input("Combien de numéro(s) de téléphone(s) voulez-vous générer ?\n")
        if nb.isdigit() == False :
            print("Veuillez entrer un nombre entier!")
            time.sleep(0.5)
        else: break
    print("Très bien nous allons vous générer", nb, "numéro(s) de téléphone(s)")
    nb_int =int(nb)
    rep = 0
    with open(file_name + ".txt", "a+") as file :
        file.write("Generation de ")
        file.write(nb)
        file.write(" numero(s) de telephone(s)\n")
        file.close()
    while rep < nb_int :
        rep = rep + 1
        num0 = "0"
        num1 ="67"
        numO = "1234567890"
        numr1 = random.choice(num1)
        numr2 = random.choice(numO)
        numr3 = random.choice(numO)
        numr4 = random.choice(num0)
        numr5 = random.choice(numO)
        numr6 = random.choice(numO)
        numr7 = random.choice(numO)
        numr8 = random.choice(numO)
        numr9 = random.choice(numO)
        head = "N"
        result_num = num0 + numr1 + numr2 + numr3 + numr4 + numr5 + numr6 + numr7 + numr8 + numr9
        print(head, rep, result_num)
        rep_str= str(rep)
        with open(file_name + ".txt", "a+") as file :
            file.write(head)
            file.write(rep_str)
            file.write(" ")
            file.write(result_num)
            file.write("\n")
            file.close()
    with open(file_name + ".txt", "a+") as file :
        file.write("Generation de ")
        file.write(nb)
        file.write(" numero(s) de telephone(s) termine!\n")
        file.write("\n")
        file.close()
    print("Génération de", nb, "numéro(s) de téléphone(s) terminé!")
    time.sleep(1)
    print("La copie des numéro(s) de téléphone(s) ce trouve dans le fichier " + file_name +".txt dans le dossier ou se trouve le script!")

else:
    what = "plaque(s) d'immatriculation(s)"
    print("D'accord nous allons générez des " + what)
    while True:
        nb = input("Combien de plaque(s) d'immatriculation(s) voulez-vous générer ?\n")
        if nb.isdigit() == False :
            print("Veuillez entrer un nombre entier!")
            time.sleep(0.5)
        else: break
    print("Très bien nous allons vous générer", nb, "plaque(s) d'immatriculation(s)")
    nb_int =int(nb)
    rep = 0
    with open(file_name + ".txt", "a+") as file :
        file.write("Generation de ")
        file.write(nb)
        file.write(" plaque(s) d'immatriculation(s)\n")
        file.close()
    while rep < nb_int :
        rep = rep + 1
        letters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        lr1 = random.choice(letters)
        lr2 = random.choice(letters)
        lr3 = random.choice(letters)
        lr4 = random.choice(letters)
        num = ("1234567890")
        numr1 = random.choice(num)
        numr2 = random.choice(num)
        numr3 = random.choice(num)
        head = "N"
        result_num = lr1 + lr2 + "-" + numr1 + numr2 + numr3 + "-" + lr3 + lr4
        print(head, rep, result_num)
        rep_str = str(rep)
        with open(file_name + ".txt", "a+") as file :
            file.write(head)
            file.write(rep_str)
            file.write(" ")
            file.write(result_num)
            file.write("\n")
            file.close()
    with open(file_name + ".txt", "a+") as file :
        file.write("Generation de ")
        file.write(nb)
        file.write(" plaque(s) d'immatriculation(s) termine!\n")
        file.write("\n")
        file.close()
    print("Génération de", nb, "plaque(s) d'immatriculation(s) terminé!")
    time.sleep(1)
    print("La copie des plaque(s) d'immatriculation(s) ce trouve dans le fichier " + file_name +".txt dans le dossier ou se trouve le script!")
