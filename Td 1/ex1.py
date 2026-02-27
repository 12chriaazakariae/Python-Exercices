try: 
    age = int(input("Entrer l'age : "))
    categorie = ""

    if(age in range(1, 13)) :
        categorie = "Enfant"    
    elif(age in range(13, 18)) :
        categorie = "Adolesent"    
    elif(age in range(18, 65)) :
        categorie = "Adult"    
    else :
        categorie = "Senior"
    print(f"tu es un {categorie}")
except ValueError:
    print("entrer un nombre valide !!!!!")
