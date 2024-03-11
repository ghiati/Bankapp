
from bank_system import SystemeBancaire 
from user import CompteUtilisateur
if __name__ == "__main__":
    systeme_bancaire = SystemeBancaire()
    systeme_bancaire.demarrer()
    user_ = CompteUtilisateur()
    user_.demarrer()


