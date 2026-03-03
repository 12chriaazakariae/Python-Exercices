donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"), 
 ("Bouchra", "Info", "abc", "G2"), 
 ("", "Math", 10, "G1"), 
 ("Yassine", "Info", 22, "G2"), 
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"), 
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Hana", "Physique", 15, "G3"), 
 ("Hana", "Math", 8, "G3"),
]

# ============= La fonction de validation =======================
def valider(enregistrement):
    nom , module , note , grp = enregistrement

    if not nom.strip() :
        return False, 'la case de nom est vide'
    if not module.strip():
        return False , 'la case de module est vide'
    if not grp.strip():
        return False , 'la case de grp est vide'
    try:
        if not note:
            return False , 'la case de note est vide'
        float_note = float(note)
        if not 0 <= float_note <=20 :
            return False , f'Note ({note}) est hors l\'intervale [0,20]'
    except ValueError:
        return False , f'Note({note}) est nom numerique'
    return True , ''

validees = []
erreurs = []
doublons_exact = set()

for data in donnees:
    if data in validees:
        doublons_exact.add(data)
        continue

    is_valide , message = valider(data)

    if is_valide :
        nom , module , note , grp = data
        success_ligne = (nom , module , float(note) , grp) 
        validees.append(success_ligne)
    else :
        dict_erreur = {
            'ligne': data,
            'raison': message
        }
        erreurs.append(dict_erreur)
        
print("# ============= Valide=======================")
for v in validees:
    print(v)

print("# ============= Erreurs=======================")
for e in erreurs:
    print(e)

print("# ============= Doublons=======================")
for d in doublons_exact:
    print(d)


module_no_repeat = set()
notes_par_etudiant = {}
etudiant_par_group = {}

for ligne in validees:
    nom, module, note, groupe = ligne
    
    module_no_repeat.add(module)

    if nom not in notes_par_etudiant :
        notes_par_etudiant[nom] = {}
    
    if module not in notes_par_etudiant[nom] :
        notes_par_etudiant[nom][module] = []

    notes_par_etudiant[nom][module].append(note)

    if groupe not in etudiant_par_group:
        etudiant_par_group[groupe] = set()

    etudiant_par_group[groupe].add(nom)

print("# ============= Modules =======================")
for m in module_no_repeat:
    print(m)

print("# ============= Notes par Etudiant =======================")
for nom, note in notes_par_etudiant.items():
    print(f"Etudiant :{nom}")
    for module , n in note.items() :
        print(f"=> {module} : {n}")

print("# ============= Etudiant par Groupe =======================")
for grp, liste_etudiants in etudiant_par_group.items():
    print(f"Groupe {grp} : {liste_etudiants}")


# =============  Calculs =======================

def somme_recursive(liste_notes):
    if len(liste_notes) == 0:
        return 0
    else:
        return liste_notes[0] + somme_recursive(liste_notes[1:]) 

def calculer_moyenne(liste_notes):
    if not liste_notes:
        return 0
    total = somme_recursive(liste_notes)
    return total / len(liste_notes)

print("\n--- Bulletins ---")
for etudiant, dossier_matieres in notes_par_etudiant.items() :
    print(f"|---Bulltin de {etudiant}---|")

    toutes_les_notes_etudiant = []
    for matiere, liste_notes in dossier_matieres.items():
        moy_mat = calculer_moyenne(liste_notes)
        print(f"{matiere} : {moy_mat:.2f}/20")

        toutes_les_notes_etudiant.extend(liste_notes)
    
    moy_gen = calculer_moyenne(toutes_les_notes_etudiant)
    print(f"Moyenne Generale: {moy_gen:.2f}/20")
    print("\n============")