# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
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
print(get_random_item_in(characters)) # j'affiche ma fonction qui a pour parametre ma liste characters

user_answer= input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme ')

if user_answer=="B":
    pass  #leave the program
if user_answer =="C":
    print("C'est pas la bonne réponse")
if user_answer== "D":
    print("tete d'alose")
else:
    pass
    #show another quotes
