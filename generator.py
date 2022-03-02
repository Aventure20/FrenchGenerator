import random
import time
import phonenumbers
from phonenumbers import carrier

visual = "//////////////////////////////////////////////////////////////////////"

print(visual)
print("ALL DATA GENERATED HERE IS BASED ON THE PATTERN OF THE FRENCH SYSTEM")
print(visual + "\n")

file_name = input("What is the name of the file where you want to save generated data?\n")

print("OK, we gonna save data in " + file_name + ".txt")
while True :
    check = input("Do you confirm? Please answer by Yes or No\n")
    check = check.lower()
    if check == "yes" : break
    if check == "y" : break
    elif check == "no" :
        file_name = input("What is the name of the file where you want to save generated data?\n")
        print("OK, we gonna save data in " + file_name + ".txt")
    elif check == "n" :
        file_name = input("What is the name of the file where you want to save generated data?\n")
        print("OK, we gonna save data in " + file_name + ".txt")
    else :
        print("Please answer by Yes or No!\n")
        

what = input("What do you want to generate?\n    1) Phone numbers\n    2) Number plates\n")
while True :
    if what == "1" : break
    elif what == "2" : break
    else :
        print("Please answer by 1 or 2\n")
        what = input("What do you want to generate?\n    1) Phone numbers\n    2) Number plates\n")

if what == "1" :
    what = "phone numbers."
    print("Ok we gonna generate", what, "Let's do this!")
    while True:
        nb = input("How many phone numbers do you want?\n")
        if nb.isdigit() == False :
            print("Please enter an integer number!")
        else: break
    print("No problem, we gonna generate", nb, "phone numbers")
    nb_int =int(nb)
    rep = 0
    with open(file_name + ".txt", "a+") as file :
        file.write("Generating ")
        file.write(nb)
        file.write(" phone numbers\n")
        file.close()
    print(visual)
    while rep < nb_int :
        num0 = "+33"
        num1 = "67"
        numO = "1234567890"
        numr1 = random.choice(num1)
        numr2 = random.choice(numO)
        numr3 = random.choice(numO)
        numr4 = random.choice(numO)
        numr5 = random.choice(numO)
        numr6 = random.choice(numO)
        numr7 = random.choice(numO)
        numr8 = random.choice(numO)
        numr9 = random.choice(numO)
        head = "N"
        result_num = num0 + numr1 + numr2 + numr3 + numr4 + numr5 + numr6 + numr7 + numr8 + numr9
        verif = phonenumbers.parse(result_num)
        if phonenumbers.is_valid_number(verif) == True: 
            rep = rep + 1            
            phone_carrier = carrier.name_for_number(verif, "en")
            print(head, rep, result_num, phone_carrier)
            print(visual)
            rep_str= str(rep)
            with open(file_name + ".txt", "a+") as file :
                file.write(head)
                file.write(rep_str)
                file.write(" // ")
                file.write(result_num)
                file.write(" // ")
                file.write(phone_carrier)
                file.write("\n")
                file.close()
        else:
            #DEBUG: print("This phone number wasn't valid.")
            continue
    print("\n")
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
