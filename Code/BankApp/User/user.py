import random


class CompteUtilisateur:
    def __init__(self, prenom, nom, email, mot_de_passe, solde=0):
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.solde = float(solde)
        self.rib = self.generer_rib()

    def generer_rib(self):
        rib = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        return rib

    def deposer(self, montant):
        try:
            montant = float(montant)  # Convert input to float
            if montant > 0:
                self.solde += montant
                print(f"{montant} déposés dans le compte de {self.prenom}.")
                self.afficher_solde()
            else:
                print("Montant de dépôt non valide.")
        except ValueError:
            print("Montant de dépôt invalide. Veuillez entrer un nombre.")

    def retirer(self, montant):
        try:
            montant = float(montant)  # Convert input to float
            if 0 < montant <= self.solde:
                self.solde -= montant
                print(f"{montant} retirés du compte de {self.prenom}.")
                self.afficher_solde()
            else:
                print("Fonds insuffisants ou montant non valide.")
        except ValueError:
            print("Montant de retrait invalide. Veuillez entrer un nombre.")

    def transfert(self, destinataire_rib, montant):
        try:
            montant = float(montant) 
            if montant > 0 and self.solde >= montant:
                print(f"Transfert de {montant} DH effectué avec succès vers le compte RIB {destinataire_rib}.")
                self.solde -= montant
            else:
                print("Montant de transfert non valide ou solde insuffisant.")
        except ValueError:
            print("Montant de transfert invalide. Veuillez entrer un nombre.")

    def afficher_solde(self):
        print(f"Solde actuel pour {self.prenom} : {self.solde} DH")

    def modifier_informations_personnelles(self, nouveau_prenom, nouveau_nom, nouveau_email, nouveau_mot_de_passe):
        self.prenom = nouveau_prenom
        self.nom = nouveau_nom
        self.email = nouveau_email
        self.mot_de_passe = nouveau_mot_de_passe
        print("Informations personnelles mises à jour avec succès.")
