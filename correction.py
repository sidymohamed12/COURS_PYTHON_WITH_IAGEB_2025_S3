# une liste c'est une comme une boite ou un sac
# on peut y mettre n'importe quoi
# on peut meme une liste dans une liste
# on utilise [] pour creer une liste
# chaque element est separe par une virgule


# ========== exo ============
# Un utilisateur est caractérisé par :
    #  – son nom complet, 
    #  – numéro de téléphone,
    #  – mot de passe,
    #  – rôle (VENDEUR, ADMIN, RESTAURATEUR)
    #  – état (1 quand il est 
    #  - actif, 0 quand il est bloqué)

# À FAIRE : 
    # – Créer une liste de 5 utilisateurs.
    # – Créer une fonction lister les utilisateurs. 
    # – Créer une fonction pour ajouter un utilisateur.
    
    
    # ===========================
    
  # Un utilisateur est caractérisé par :
    #  – son nom complet, 
    #  – numéro de téléphone,
    #  – mot de passe,
    #  – rôle (VENDEUR, ADMIN, RESTAURATEUR)
    #  – état (1 quand il est actif, 0 quand il est bloqué)
    
# utilisateur1 = [
    # 0 -> "sidy mohamed", 
    # 1 -> "761823698", 
    # 2 -> "passer", 
    # 3 -> "RESTAURATEUR", 
    # 4 -> "1"]
    
utilisateurs = [
    ["sidy mohamed", "761823698", "passer", "RESTAURATEUR", "1"],
    ["mame awa", "771234567", "passer", "ADMIN", "1"],
    ["kim mich", "779876543", "passer", "VENDEUR", "0"]
]


def afficher_utilisateur(listeUtilisateurs):
    print("============== liste des utilisateurs ==============")
    cpt = 0
    for utilisateur in listeUtilisateurs:
        cpt = cpt + 1
        nom = utilisateur[0]
        numero = utilisateur[1]
        mdp = utilisateur[2]
        role = utilisateur[3]
        etat_recuperer = utilisateur[4]
        etat_a_afficher = "actif" if etat_recuperer == "1" else "bloque"
    
        print(f"utilisateur n° {cpt}")
        print(f"nom : {nom} , numero : {numero} , mdp : {mdp} , role : {role} , etat : {etat_a_afficher}")
        print("-" * 30)
        
# afficher_utilisateur(utilisateurs)


def ajout_utilisateur():
    print("------------- ajout d'utilisateur -------------")
    utilisateur_a_ajouter = []
    
    nom = input("entrer le nom de l'utilisateur : ")
    numero = input("entrer le numero de l'utilisateur : ")
    mdp = input("entrer le mdp de l'utilisateur : ")
    role = input("entrer le role de l'utilisateur : ")
    while role.upper() not in ["VENDEUR", "ADMIN", "RESTAURATEUR"]:
        print("le role doit etre VENDEUR, ADMIN ou RESTAURATEUR")
        role = input("entrer le role de l'utilisateur : ")
        
    etat = 1
    
    utilisateur_a_ajouter.extend([nom, numero, mdp, role.upper(), etat])
    
    utilisateurs.append(utilisateur_a_ajouter)
    
    print("------- UTILISATEUR AJOUTER AVEC SUCCESS -------")
