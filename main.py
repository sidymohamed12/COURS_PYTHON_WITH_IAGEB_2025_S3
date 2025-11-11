
# une liste c'est une comme une boite ou un sac
# on peut y mettre n'importe quoi
# on peut meme une liste dans une liste
# on utilise [] pour creer une liste
# chaque element est separe par une virgule

fruits = [
            "pomme", "banana", "orange", 
            # ["kiwi", "ananas"]
        ]

# CRUD -> create, read, update, delete

# ========= CREATION DE LISTE ==========

# un plat est caracterise par :
    # - son nom
    # - Quantite en stock
    # - prix de vente
    # - ses ingredients
    # - sa disponibilite

# ingredients = [
#     "huile", "riz", "poisson"
# ]

plat = ["Thiebou Dieune", 5, 1200, ["huile", "riz", "poisson"], 1 ]
plat2 = ["mafe", 3, 1000, ["huile" , "viande", "arachide"], 1]
plat3 = ["yassa boulette",10,950,["oignon ","riz","bissap"],1]
plat4 = ["yassa" , 10 , 50 , [ "Riz" , "viande", "oignons" ],1]

plats = [
    ["Thiebou Dieune", 5, 1200, ["huile", "riz", "poisson"], 1 ],
    ["mafe", 3, 1000, ["huile" , "viande", "arachide"], 1],
    ["yassa boulette", 10, 950, ["oignon ", "riz", "bissap"], 1],
    ["yassa" , 10 , 50 , [ "Riz" , "viande", "oignons" ],1]
]


# ============ AFFICHAGE DE LISTE ===========

#  pour plat

# plat = [
            # 0  ->    "Thiebou Dieune", 
            # 1  ->     5, 
            # 2  ->     1200, 
            # 3  ->     ["huile", "riz", "poisson"], 
            # 4  ->     1 
        # ]
  

# print(plat[0])
# print(plat[1])
# print(plat[2])
# print(plat[3])
# print(plat[4])

#  pour plats :

# plats = [
    # 0 -> ["Thiebou Dieune", 5, 1200, ["huile", "riz", "poisson"], 1 ],
    # 1 -> ["mafe", 3, 1000, ["huile" , "viande", "arachide"], 1],
    # 2 -> ["yassa boulette", 10, 950, ["oignon ","riz","bissap"], 1],
    # 3 -> ["yassa" , 10 , 50 , [ "Riz" , "viande", "oignons" ],1]
# ]

# print(plats[0])
# print(plats[1])
# print(plats[2])
# print(plats[3])

# pour recuperer un element de la liste de plats :

# print(plats[2][0])

# fonctions pour recuperer les elements de plats
def afficher_plat(listePlats) :
    cpt = 0
    for plat in listePlats :
        cpt = cpt + 1
        
        nom = plat[0]
        quantite = plat[1]
        prix = plat[2]
        ingredients = plat[3]
        disponibilite = plat[4]
        
        # print ("nom : " + nom + "  quantite : " + quantite)
        # print (f"nom : {nom} quantite : {quantite}")
        
        print(f"plat n° {cpt}")
        print(f"nom plat : {nom}, quantite : {quantite}, prix : {prix}, disponibilite : {disponibilite}, ingredients : {ingredients}")
        # print("ingredients : ")
        # for ing in ingredients :
        #     print(ing)

        print("\n")
        
# afficher_plat(plats)



# ============= CREATION DE PLATS ============

# on 2 possibilite pour ajouter dans une liste :
    # - la methode append -> ajoute un element a la fin de la liste (si c'est une liste, il ajoute la liste entiere)
    # - la methode extend -> ajoute plusieurs elements a la fin de la liste (si c'est une liste, il ajoute les elements de la liste entiere)

#  pour append :

    # print("aaaavvaannnttt ajout")
    # print(plat)

    # plat.append("senegalais")


    # print("aaappppreeeeessss ajout")
    # print(plat)

# pour extend :
    # print("aaaavvaannnttt ajout")
    # print(plat)

    # plat.extend(["senegalais", "francais", "italien"])

    # print("aaappppreeeeessss ajout")
    # print(plat)
    

def ajout_plat():
    print("-------------- ajout de plat --------------")
    plat_a_ajouter = [
    ]
    
    nom = input("entrer le nom du plat : ")
    quantite = input("entrer la quantite du plat : ")
    prix = input("entrer le prix du plat : ")
    disponibilite = 1
    ings = []
    ok = input("voulez-vous ajouter des ingredients ? (o/n) : \n")
    while ok == "o":
        ing = input("entrer l'ingredient : ")
        ings.append(ing)
        ok = input("voulez-vous ajouter des ingredients ? (o/n) : ")
    
    # avec append
    # plat_a_ajouter.append(nom)
    # plat_a_ajouter.append(quantite)
    # plat_a_ajouter.append(prix)
    # plat_a_ajouter.append(ings)
    # plat_a_ajouter.append(disponibilite)
    
    # avec extend
    plat_a_ajouter.extend([nom, quantite, prix, ings, disponibilite])
    
    plats.append(plat_a_ajouter)
    
    print("------- PLAT AJOUTER AVEC SUCCESS -------")
    
    afficher_plat(plats)
    
print("------------- avant insertion -------------")
afficher_plat(plats)
print("--------------------------------------- \n")

ajout_plat()