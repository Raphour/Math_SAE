#Importation
from re import X
import numpy as np
import copy
import time 

def abs(x):
    if x<0:
        return -x
    return x
def evaluer_clause(clause,list_var):
    '''Arguments : une liste d'entiers non nuls traduisant une clause,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
'''
    if len(clause) == 0:
        return False
    
    for x,y in zip(clause, list_var):
        y = list_var[abs(x)-1]
            
        if x >0 and y == True :
            return True
        elif x<0 and y == False:
            return True
        elif y == None:
            return None

            
    return False

def evaluer_cnf(formule,list_var):
    '''Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
'''
    for clause in formule:
        if evaluer_clause(clause, list_var) == False:

            return False
        elif evaluer_clause(clause, list_var) == None:
            return None
    return True


def determine_valuations(list_var):
    '''Arguments : une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var

'''
    valuations = []
    indices = [i for i in range(len(list_var)) if list_var[i] == None]
    for i in range(2**len(indices)):
        valuation = copy.deepcopy(list_var)
        for j in range(len(indices)):
            valuation[indices[j]] = (i // 2**j) % 2 == 1
        valuations.append(valuation)	
    return valuations

def resol_sat_force_brute(formule,list_var):
    valuations = determine_valuations(list_var)
    for valuation in valuations:
        if evaluer_cnf(formule, valuation) == True:
            return True, valuation
    return False, []


def enlever_litt_for(formule,litteral):
    '''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''
    for i in range(len(formule)-1,-1,-1):#Pour toute les clauses de la formules
        for j in range(len(formule[i])):#Pour tous les litteraux de la clause
            if litteral==formule[i][j]:
                del formule[i]
                break
            if litteral == -formule[i][j]:
                del formule[i][j]
                break
    return formule

def init_formule_simpl_for(formule_init,list_var):
    for i in range(len(list_var)):
        if list_var[i]==True:
            litteral=i+1
            enlever_litt_for(formule_init,litteral)
        if list_var[i]==False:
            litteral=-i-1
            enlever_litt_for(formule_init,litteral)
    return formule_init

def retablir_for(formule_init,list_chgmts):
    # Créer une liste des variations
    # Copie de la formule
    formule = copy.deepcopy(formule_init)
    list_var = [None for i in range(max(max(list_chgmts))+1)]
    # Ajouter les variations
    for changement in list_chgmts:
        list_var[changement[0]] = changement[1]
    # Simplifier la formule
    formule = init_formule_simpl_for(formule,list_var)

    return formule