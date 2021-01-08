# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

#Voici la liste des actions de ma fonction , une fonction
#principale qui regroupe un ensemble de petites actions
#show random quote (afficher une citation au hasard)
    # get a random number (obtenir un nombre aléatoire)
    # get a quote from a list (obtenir une citation d'une liste)
    # show the quote in the interpreter (afficher la citation dans l'interpréteur)

def get_random_quote():
    pass

def get_random_item_in(my_list): # je défini ma fonction qui aura pour parametre une liste
## TODO: : get a random item  (obtenir un objet au hasard)
    item = my_list[1] # ma variable "item" sera l'objet index 1 de la liste #get an item from a list. For the moment just get de firt one( obtenir un objet d'une liste. pour le moment obtenir le 1er)
    #TODO: show the quote
    #print(item) #j'affiche ma variable item
    return item #je retourne ma variable item



user_answer= input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme ')

while user_answer!= "B":
  print(get_random_item_in(quotes)) # j'affiche ma fonction qui a pour parametre ma liste characters
  user_answer= input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme ')

for personnage in characters:#pour chaque élément dans cette list fait ça.
                    # dans cette ligne il y a deux variable : item et a_list
  personnage_name= personnage.capitalize()
  print(personnage_name)



#print(get_random_item_in(quotes))
