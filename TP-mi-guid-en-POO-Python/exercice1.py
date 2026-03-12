from abc import ABC, abstractmethod
from dataclasses import dataclass

# ========================================================================
class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f"Commande : {self.description()} \n Prix: {self.cout()} $"



    def __add__(self, other):
        nouvelle_desc = self.description() + " et " + other.description()
        nouvelle_prix = self.cout() + other.cout()

        return BoissonMerging(nouvelle_desc, nouvelle_prix)

# ========================================================================
@dataclass    
class Client:
    nom : str
    numero : int
    points_fidelite : int

# ========================================================================
class Cafe(Boisson):

    def cout(self):
        return 2.0 

    def description(self):
        return "Cafe simple "    
# ========================================================================
class The(Boisson):
    def cout(self):
        return 1.5
    
    def description(self):
        return "Thé"
# ========================================================================
class DecorateurBoisson(Boisson) :
    def __init__(self, boisson) :
        self._boisson = boisson

# ========================================================================
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    
    def description(self):
        return self._boisson.description() + ", Lait"
    
# ========================================================================
    
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"
    

# ========================================================================
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.4
    
    def description(self):
        return self._boisson.description() + ", Caramel"



# ========================================================================
class BoissonMerging(Boisson):
    def __init__(self, description, prix):
        self._description = description
        self._prix = prix

    def cout(self):
        return self._prix
    
    def description(self):
        return self._description


# ========================================================================
class Commande:
    def __init__(self , client):
        self.boissons = []
        self.client = client

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def calculer_totale(self):
        prix_totale = 0
        for boisson in self.boissons:
            prix_totale +=  boisson.cout()

        return prix_totale

    def afficher_commande(self):
        print(f"Client : {self.client.nom}")
        print(f'les commandes sont : ')
        for commande in self.boissons:
            print(f"\t -{commande.description()} -> {commande.cout()} $     ")

        print(f"Prix totale : {self.calculer_totale()} $")


# ========================================================================
class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print(f'\n=======Commande Sur Place ===========')
        super().afficher_commande()
class CommandeEmporter(Commande):
    def afficher_commande(self):
        print(f'\n=======Commande Sur Emporter ===========')
        super().afficher_commande()



# ========================================================================
class Fidelite:
    def ajouter_points(self, client, montant):
        client.points_fidelite += int(round(montant))


# ========================================================================
class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        totale = self.calculer_totale()
        self.ajouter_points(self.client, totale)
        print(f'Commande validee points actuelle du client : {self.client.points_fidelite}')    
        

# ========================================================================

boisson = Cafe()
boisson = Lait(boisson)
# print(boisson)

boisson1 = The()

boisson1 = Sucre(boisson1)
# print(boisson1)

boisson2 = Cafe()

boisson2 = Lait(boisson2)
boisson2 = Sucre(boisson2)
# print(boisson2)

client1 = Client(nom="Zakariae", numero=1, points_fidelite=0)
ma_cmd = CommandeFidele(client1)
ma_cmd.ajouter_boisson(boisson)
ma_cmd.ajouter_boisson(boisson1)
ma_cmd.ajouter_boisson(boisson2)
ma_cmd.afficher_commande()
ma_cmd.valider_commande()


