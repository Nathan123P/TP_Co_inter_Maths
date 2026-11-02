#Une variable est toujours ecrite sans espace
#elle commence par une minuscule et chaque mot qui suit a une majuscule 
jeSuisUneVariable = 1  #<-- variable ecrite correctement car en relisant onn sait a quoi elle correspond

#Une constante est ecrite en MAJUSCULE
PI = 3.14

#Une variable peut contenir un nombre
jeSuisUneVariable0 = 10
#afficher une variable 
print("La valeur est : " + str(jeSuisUneVariable0))
jeSuisUneVariable0 = 11
print("La valeur est : " + str(jeSuisUneVariable0))



#Une variable peut contenir une chaine de caractere 
jeSuisUneVariable2 = "Coucou"

#Une variable peut contenir un booleen
jeSuisUneVariableTableauBoleen1 = True

#Une variable peut contenir un booleen
jeSuisUneVariableBolleen2 = 3.14

#Une variable peut contenir un tableau et ce tableau ^peut contenir une variable, un boleen, un tableau
jeSuisUneVariableTableau1 = [1, "Eleve1", True, ["Eleve2, 12, 1.2, True"] ]


#Calcule 
uneVariable1 = 1
uneVariable2 = 3
total = uneVariable1 + uneVariable2
print("Le total est :" + str(total))

#compare deux variabes 
#les tests sont : ==, !=, <, >, <=, >=
#/!\ on met == pour tester une egalite 
#if (condition): 
if uneVariable1 == uneVariable2:
    #si vrai 
    print("Les deux variables sont egales")
else:
    #si faux
    print("Les deux variables sont differentes")
    

#saisi  
monNom = input("Veuillez saisir un nom : ") #<-- ici c'est une chaine de caractere qui doit etre saisi
