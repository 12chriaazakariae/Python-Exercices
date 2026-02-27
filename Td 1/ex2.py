contacts = [
    {'nom' : 'ahmed', 'tele' : '06123'},
    {'nom' : 'zakariae', 'tele' : '06456'},
    {'nom' : 'amine', 'tele' : '06789'}
]

# ajouter
def ajouter_contact(contacts):
    nom = input('entrer le nom a ajouter : ')
    tele = input('entrer le numero : ')
    while len(tele) != 5 : 
        print("tele doit contenir 5 numero !!")
        tele = input('entrer le numero : ')

    new_contact = {'nom':nom, 'tele' : tele}
    contacts.append(new_contact)
# afficher
def afficher_contact(contacts):
    for i,contact in enumerate(contacts) :
        print(f"{i+1} = {contact}")

# supprimer
def supprimer_contact(contacts) :
    exist = False
    while not exist :
        nom_a_supprimer = input("Entrer le nom du contact a supprimer : ")
        for i,c in enumerate(contacts):
            if nom_a_supprimer == c['nom'] :
                contacts.pop(i)
                print(f"le contact {nom_a_supprimer} supprimer!!")
                exist = True
                break
        if not exist :
            print("Element nom trouver , Ressayez !!") 
# ===========================================================
print("Contacts : \nPour ajouter un contact entrer 1 \nPour ajouter un contact entrer 2 \npPour afficher les contacts entrer 3 ")
operations = {1 , 2 , 3}
commande = int(input("entrer la commande (1 , 2 ou 3) : ")) 
while(commande not in operations) :
    print ('il faut entrer 1 , 2 ou 3 !!!')
    commande = int(input("entrer la commande (1 , 2 ou 3) : ")) 

match commande:
    case 1 :
        ajouter_contact(contacts)
        afficher_contact(contacts)
    case 2 :
        afficher_contact(contacts)
    case 3 :
        supprimer_contact(contacts)
        