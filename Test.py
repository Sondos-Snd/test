# # Test
# # This document was originally created on a Jupyter notebook

# ## Ex 1
# ### Écrire une fonction qui prend un paramètre chaîne de caractère et qui renvoi cette chaine en majuscule, sans utiliser la fonction majus directement.

import string

def makeUppercase( userInput ): 
    #check input value
    if isinstance(userInput, str): 
        #grab seperate letters
        for letter in userInput:
            #exclude spcial cases
            if (letter not in string.ascii_uppercase) and (letter.isalpha()):
                #make uppercase
                userInput=userInput.replace(letter, chr(ord(letter) - 32 )) 
        #return input
        return "The capital letters format of this value is : " + userInput
        
    else: 
        return "please enter a string value"

    #interact with user
print ('Enter a string value')
userInput = input('User value: ')

#call the function
makeUppercase( userInput )


# ## Ex 2
# ### Écrire une fonction qui prend un paramètre entier X, et qui renvoi une réponse booléenne pour dire si le chiffre est divisible par 3 ou pas, sans utiliser la fonction div ou mod ou les opérateurs de division et reste de la division.


#this function checks whether an integer can be devised by 3
def checkIfDiv3( userInput ):
    #check if numeric input
    if userInput.isdigit():
        
        #if the sum of integer digits can be devised by 3, the integer can too
        #calculate sum of digits
        referenceValue= sum(map(float,userInput))
        
        #fix starting point
        x=0
        #try the reach the input value
        while x < referenceValue:
            x+=3
        
        #if reached value:
        if x==referenceValue:
            return "Your value (" + userInput + ") is divisible by 3"
        
        #if exceeded value..
        else:
            return "Your value (" + userInput + ") is not divisble by 3"
        
    else: 
        return "Please enter a float value"

#get the user input
print ('Enter a float value')
userInput = input('Value: ')

checkIfDiv3( userInput )


# ## Ex 3
# 
# ### Plateau= [ [True , False , False , False ] ,  [ False , True , True , False ] ]
# 
# ### Un plateau est un tableau à deux dimensions qui contient des Booléens. Si plateau[i][j] vaut True, il y a un mur et sinon la case est libre.
# 
# ### Le but de l'exercice est d'écrire une fonction chemin prenant un plateau et les coordonnées de deux cases deb et fin et renvoie True si l'on peut aller de la case deb à la case fin en se déplaçant horizontalement et verticalement.
# 
# ### Dans notre exemple, chemin(plateau,(1,3),(1,0)) renverra False et chemin(plateau,(1,3),(0,1)) renverra True.
# 
# ### Ecrire une fonction voisinsCase qui prend un plateau et une case et renvoie l'ensemble de ces voisins immédiats horizontaux ou verticaux qui sont sur le plateau et qui sont libres.
# 
# ### Ecrire une fonction voisinsCases qui prend un plateau et un ensemble de cases et renvoie l'ensemble de tous les voisins de ces cases.
# 
# ### Ecrire une fonction accessibles qui prend un plateau et une case et renvoie l'ensemble des cases que l'on peut atteindre depuis cette case en se déplaçant horizontalement et verticalement.
# 
# ### Ecrire la fonction chemin.



refCase=(1,7)

#this functions takes the plateau, the case, and returns the neighbor cases that can be accessed
def voisinsCase(Plateau,refCase):
    
    #get the cases's vertical and horizental positions
    vRef=refCase[0]
    hRef=refCase[1]
    
    #Check whether the vertical neighbor is up or down the reference case
    if vRef==0:
        verticalCase=[(vRef+1,hRef),Plateau[vRef+1][hRef]]
    else:
        verticalCase=[(vRef-1,hRef),Plateau[vRef-1][hRef]]
        
    #check if the referene case is at an extrimity of a row 
    if hRef==0:
        leftCase=[(vRef,hRef-1),True]
        rightCase=[(vRef,hRef+1),Plateau[vRef][hRef+1]]
        
    elif hRef==len(Plateau[0])-1:
        leftCase=[(vRef,hRef-1),Plateau[vRef][hRef-1]]
        rightCase=[(vRef,hRef+1),True]
 
    #case of we are in the middleof a row
    else:
        leftCase=[(vRef,hRef-1),Plateau[vRef][hRef-1]]
        rightCase=[(vRef,hRef+1),Plateau[vRef][hRef+1]]

    #list of possible neighbors
    Neighbours=[verticalCase,rightCase,leftCase] 
    
    ##check if neighbor cases are accessible
    freeNeighbours=[]
    for i in range(0,len(Neighbours)):
        if Neighbours[i][1]==False:
            freeNeighbours.append(Neighbours[i][0])    
    
    return freeNeighbours

#call the funtion
voisinsCase(Plateau,refCase)





listCases=[(1,3),(0,2),(1,7)]

def voisinsCases(Plateau,listCases): 
    
    #Get, for all cases in the list, all the cases' neighbors
    #result format : [ tuple(ref case) : liteOfTuples(neighbors)]
    listNeighbors=[] 
    for i in range(0,len(listCases)):    
        listNeighbors.append( [listCases[i],voisinsCase(Plateau,listCases[i])] )
        
    return listNeighbors

voisinsCases(Plateau,listCases)




#example
Plateau= [ [True , False , False , False, True , False , False , False ] ,
          [ False , True , True , False, True , False , False , False ] ]
startCase=(1,3)

#initialize the recursive reference
visited=[]

#this function detects all of the possibly accessible cases for a given reference case
def accessibles(Plateau,startCase): 
    
    access=[]

    #detect all accessible mmediate neighbors
    for x in range(0,len(voisinsCase(Plateau,startCase))):
        access.append(voisinsCase(Plateau,startCase)[x])
    
    #get ot list of the cases that can be accessed , starting from your new list of cases
    listVoisins=voisinsCases(Plateau,voisinsCase(Plateau,startCase))
    
    #for each voisin case, define and iterate on the list of the possible cases
    for i in range(0,len(listVoisins)):
        for j in range(0,len(listVoisins[i][1])):
            
            #grab the values contained in this format : [ tuple(ref case) : liteOfTuples(neighbors)]            
            secondVoisins=voisinsCase(Plateau,listVoisins[i][1][j])
            
            for k in range(0,len(voisinsCase(Plateau,listVoisins[i][1][j]))-1):
                
                #Consider and save the reachable cases
                if secondVoisins[k] not in listVoisins[i][1][j]:
                    if secondVoisins[k] not in access:
                        access.append(secondVoisins[k])
    
    #save the visited case to avoid repetition
    if startCase not in visited:
        visited.append(startCase)
    
    #save all possible routes
    chemins=access
    
    #recursive funtion calling
    for i in range(0,len(access)):
        if access[i] not in visited:
            chemins.append(accessibles(Plateau,access[i]))
    
    #return a clean non repetitive list of possible routes
    return visited

accessibles(Plateau,startCase)





startCase=(1,3)
endCase=(0,1)

#tis is the main funtion
def Chemin(Plateau,startCase,endCase):
    
    #call the cases that can be reached
    #check if endCase is in there
    if endCase in accessibles(Plateau,startCase):              
        return True
    else:
        return False

#call the final funtion
Chemin(Plateau,startCase,endCase)

