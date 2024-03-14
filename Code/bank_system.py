import re
from user import CompteUtilisateur
from BankDatabase import users_collection, historique_collection
from Insert_user import InsertUsers

class SystemeBancaire:
    def __init__(self):
        self.comptes_utilisateurs = {}

    def valider_email(self, email):
        motif = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(motif, email)

    def valider_mot_de_passe(self, mot_de_passe):
        return len(mot_de_passe) >= 8

    def valider_nom(self, nom):
        return len(nom) > 0

    def valider_rib(self, rib):
        return re.match(r'^[0-9]{12}$', rib)

    def connexion(self, email, mot_de_passe):
        for compte in self.comptes_utilisateurs.values():
            if compte.email == email and compte.mot_de_passe == mot_de_passe:
                print("Connexion réussie !")
                return compte
        print("Email ou mot de passe invalide.")
        return None

    def inscription(self, prenom, nom, email, mot_de_passe, rib):
        if self.valider_email(email) and self.valider_mot_de_passe(mot_de_passe) and \
                self.valider_nom(prenom) and self.valider_nom(nom) and self.valider_rib(rib):
            if email not in [utilisateur.email for utilisateur in self.comptes_utilisateurs.values()]:
                nouveau_compte = CompteUtilisateur(prenom, nom, email, mot_de_passe, rib)
                self.comptes_utilisateurs[email] = nouveau_compte
                print("Compte créé avec succès !")
                return nouveau_compte
            else:
                print("Email déjà existant.")
        else:
            print("Format d'email, mot de passe, nom, ou RIB invalide.")
        return None

    def traiter_transaction(self, compte, option):
        if option == '1':
            montant = float(input("Entrez le montant à déposer : "))
            compte.deposer(montant)
        elif option == '2':
            montant = float(input("Entrez le montant à retirer : "))
            compte.retirer(montant)
        elif option == '3':
            compte.afficher_solde()
        elif option == '4':
            print("Déconnexion réussie !")
        elif option == '5':
            rib_destinataire = input("Entrez le RIB du destinataire : ")
            montant = float(input("Entrez le montant à transférer : "))
            if rib_destinataire in [utilisateur.rib for utilisateur in self.comptes_utilisateurs.values()]:
                compte.transfert(rib_destinataire, montant)
            else:
                print("Destinataire non trouvé.")
        elif option == '6':
            nouveau_prenom = input("Entrez le nouveau prénom : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouveau_email = input("Entrez le nouvel email : ")
            nouveau_mot_de_passe = input("Entrez le nouveau mot de passe : ")
            compte.modifier_informations_personnelles(nouveau_prenom, nouveau_nom, nouveau_email, nouveau_mot_de_passe)
        else:
            print("Option invalide. Veuillez réessayer.")

    def demarrer(self):
        print("Bienvenue dans le Système Bancaire Console !")
        print("-------------------------------------")

        while True:
            print("\nMenu :")
            print("1. Connexion")
            print("2. Inscription")
            print("3. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == '1':
                email = input("Entrez votre email : ")
                mot_de_passe = input("Entrez votre mot de passe : ")
                compte = self.connexion(email, mot_de_passe)

                if compte:
                    while True:
                        print("\nMenu du Compte :")
                        print("1. Dépôt")
                        print("2. Retrait")
                        print("3. Vérifier Solde")
                        print("4. Déconnexion")
                        print("5. Transfert d'argent")
                        print("6. Modifier Informations Personnelles")

                        option = input("Entrez votre option : ")
                        if option == '4':
                            break
                        self.traiter_transaction(compte, option)

            elif choix == '2':
                prenom = input("Entrez votre prénom : ")
                nom = input("Entrez votre nom : ")
                email = input("Entrez votre email : ")
                mot_de_passe = input("Entrez votre mot de passe : ")
                rib = input("Entrez votre RIB (12 chiffres) : ")
                InsertUsers.inscription_users(prenom, nom, email, mot_de_passe, rib)
                compte = self.inscription(prenom, nom, email, mot_de_passe, rib)

                if compte:
                    
                    while True:
                        print("\nMenu du Compte :")
                        print("1. Dépôt")
                        print("2. Retrait")
                        print("3. Vérifier Solde")
                        print("4. Déconnexion")
                        print("5. Transfert d'argent")
                        print("6. Modifier Informations Personnelles")

                        option = input("Entrez votre option : ")
                        if option == '4':
                            break
                        self.traiter_transaction(compte, option)

            elif choix == '3':
                print("Merci d'utiliser le Système Bancaire Console !")
                break

            else:
                print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    systeme_bancaire = SystemeBancaire()
    systeme_bancaire.demarrer()
