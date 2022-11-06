from re import X
#import numpy as np
import copy
import time

#DEUX PETITES FONCTIONS DE TEST UTILISEES PLUS BAS#
def test(mess,eval,res):
    print(mess,(eval==res)*'OK'+(eval!=res)*'Try again')
def test_determine_valuations(mess,list_var,res):
    test=mess+'Ok'
    list_testee=determine_valuations(list_var)
    for el in list_testee :
        if el not in res:
            test=mess+'Try again'
            return test
    for el in res:
        if el not in list_testee :
            test=mess+'Try again'
            return test
    for i in range(len(list_testee)-1):
        if list_testee[i] in list_testee[i+1:]:
            test=mess+'wowowow y a du doublon là-dedans'
            return test
    return test  

#A VOUS DE JOUER#

def abs(x):
    if x<0:
        return -x
    else:
        return x


    

def evaluer_clause(clause,list_var):
    '''Arguments : une liste d'entiers non nuls traduisant une clause,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
'''
    if len(clause) == 0:
        return False
    
    for x,y in zip(clause, list_var):
        if abs(x)-1 == list_var.index(y):
            if x >0 and y == True :
                return True
            elif x<0 and y == False:
                return True
            elif y == None:
                return None
        else:
            y = list_var[abs(x)-1]
            if x >0 and y == True :
                return True
            elif x<0 and y == False:
                return True
            elif y == None:
                return None
            
    return False

# clause1=[1,-2,3,-4]
# list_var1=[True,True,False,None]
# test("essai cas 1 evaluer_clause : ",evaluer_clause(clause1,list_var1),True)
# clause2=[1,-2,3,-4]
# list_var2=[False,True,False,None]
# test("essai cas 2 evaluer_clause : ",evaluer_clause(clause2,list_var2),None)
# clause3=[1,-2,3,-4]
# list_var3=[None,True,False,True]
# test("essai cas 3 evaluer_clause : ",evaluer_clause(clause3,list_var3),None)
# clause4=[2,-3]
# list_var4=[False,False,True,False]
# test("essai cas 4 evaluer_clause : ",evaluer_clause(clause4,list_var4),False)
# clause5=[]
# list_var5=[False,False,True]
# test("essai cas 5 evaluer_clause : ",evaluer_clause(clause5,list_var5),False)

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
    
# for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
# list_var_for1_test1=[True,False,False,None]
# test('test1 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test1),True)
# list_var_for1_test2=[None,False,False,None]
# test('test2 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test2),None)
# list_var_for1_test3=[True,False,True,False]
# test('test3 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test3),False)

def determine_valuations(list_var):
    '''Arguments : une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var

'''
    valuations = []
    def replace_none(list_var):
        
        for i in range(len(list_var)):
            if list_var[i] == None:
                copy_list_var = copy.deepcopy(list_var)
                copy_list_var[i] = True
                copy_list_var2 = copy.deepcopy(list_var)
                copy_list_var2[i] = False
        return [copy_list_var, copy_list_var2]
                

    if None not in list_var:
        return [list_var]
    else:

        replace_true, replace_false =  replace_none(list_var)	
        valuations.append(replace_false)
        valuations.append(replace_true)
        print("valuations", valuations)
        print (replace_true, replace_false)

    

    valuations = "oui"
    return valuations
    
    

determine_valuations([None,None])


    # n = len(list_var)
    # ensemble_valuations = []
    # une_valuation = []
    # valuations_finales = []
    # for m in range(n):
    #     lenght = 2**n
    #     changement = lenght / (2**(m+1))
       
    #     bit : bool = False
    #     une_valuation = []
    #     for i in range(lenght):
    #         if i%changement == False and i!=False:
    #             bit = not(bit)
    #             une_valuation.extend([bit])
    #         else:
    #             une_valuation.extend([bit])
    #     ensemble_valuations.append(une_valuation)
    # for x in zip(*ensemble_valuations):
    #     x = list(x)
    #     avancement = 0
    #     for i in range(len(x)): 
    #         if (list_var[i]==None):
    #             avancement += 1
    #         elif x[i] == list_var[i]:
    #             avancement +=1
                
                
    #     if avancement == len(x):
    #         valuations_finales.append(x)
    # return(valuations_finales)

# list_var1=[True,None,False,None]
# print(test_determine_valuations('res_test_determine_valuations cas 1 : ',list_var1,[[True, True, False, True], [True, False, False, True], [True, True, False, False], [True, False, False, False]]))
# list_var2=[None,False,True,None,True,False]
# print(test_determine_valuations('res_test_determine_valuations cas 2 : ',list_var2,[[True, False, True, True, True, False], [False, False, True, True, True, False], [True, False, True, False, True, False], [False, False, True, False, True, False]]))
# list_var3=[False,True,True,False]
# print(test_determine_valuations('res_test_determine_valuations cas 3 : ',list_var3,[[False, True, True, False]]))
# list_var4=[None,None,None]
# print(test_determine_valuations('res_test_determine_valuations cas 4 : ',list_var4,[[True, True, True], [False, True, True], [True, False, True], [False, False, True], [True, True, False], [False, True, False], [True, False, False], [False, False, False]]))


def resol_sat_force_brute(formule,list_var):
    valuations = determine_valuations(list_var)
    for valuation in valuations:
        if evaluer_cnf(formule, valuation) == True:
            
            return True, valuation
    return False, []
            
    
    
    '''
    Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide
    '''
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var_for1_test1=[True,False,False,None]
test('test1 resol_sa_force_brut: ',resol_sat_force_brute(for1,list_var_for1_test1),(True, [True,False,False,False]))


def init_formule_simpl_for(formule_init,list_var):
    '''
    Renvoie : La formule simplifiée en tenant compte des valeurs logiques renseignées dans list_var
'''
    for clause in formule_init:
        if evaluer_clause(clause,list_var) == True:
            formule_init.remove(clause)
    return formule_init
for1=[[1,2],[-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var = [True,None,None,None]




def enlever_litt_for(formule,litteral):
    '''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''
    
'''for1=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt1=4
test('essai cas 1 enlever_litt_for : ',enlever_litt_for(for1,litt1),[[-1, 2, 3], [-1, -2, -5], []])'''

def retablir_for(formule_init,list_chgmts):
    '''Arguments : une formule initiale et une liste de changements à apporter sur un ensemble de variables (chaque changement étant une liste [i,bool] avec i l'index qu'occupe la variable dans list_var et bool la valeur logique qui doit lui être assignée) 
    Renvoie : la formule simplifiée en tenant compte de l'ensemble des changements
'''

'''
formule_init:  [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]]
list_chgmts1 : [[0, True], [1, True], [2, False]]
form1 : [[-5], [4, 5], [-4, 5]]

list_chgmts2 : [[0, True], [1, True], [2, False], [3, True], [4, False]]
form2 : [[]]

list_chgmts3 : [[0, True], [1, True], [2, False], [3, False]]
form3 : [[-5], [5]]
test('essai cas 1 retablir_for : ',retablir_for(formule_init,list_chgmts1),form1)
test('essai cas 2 retablir_for : ',retablir_for(formule_init,list_chgmts2),form2)
test('essai cas 3 retablir_for : ',retablir_for(formule_init,list_chgmts3),form3)
'''

def progress(list_var,list_chgmts):
    '''Arguments : list_var, list_chgmts définies comme précédemment
    Renvoie : l1,l2
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def progress_simpl_for(formule,list_var,list_chgmts):
    '''Arguments : formule,list_var, list_chgmts définies comme précédemment
    Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour):
    '''Arguments : list_sans_retour contient l'ensemble des numéros de variables auxquelles on a affecté une valeur logique sur laquelle on ne reviendra pas
    renvoie :form,l1,l2,l3 avec :
    form : la formule simplifiée
    l1 : la liste actualisée des valeurs attribuées aux variables après le changement effectué
    l2 : la liste actualisée de l'ensemble des changements effectués
    l3 : la liste éventuellement actualisée des numéros de variables auxquelles une affectation a été attribuée sur laquelle on ne reviendra pas
    '''
    

def retour(list_var,list_chgmts):
    '''
    renvoie :l1,l2 avec :
    l1 : la liste actualisée des valeurs attribuées aux variables 
    l2 : la liste actualisée de l'ensemble des changements effectués depuis une formule initiale
    
    '''

def retour_simpl_for(formule_init,list_var,list_chgmts):
    '''
Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour):
    '''
Renvoie : form,l1,l2,l3
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts
    l3 : nouvelle list_sans_retour
'''
    
def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    '''Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide'''
    
    

def resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts):#la même distinction peut être faite entre formule et formule_init
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
''' 
        


def resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
'''

        
def ultim_resol(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for_dpll(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def creer_grille_init(list,n):
    '''Arguments : une liste de listes(contenant les coordonnées à renseigner et le nombre correspondant) et un entier donnant la taille de la grille
        Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''
    
def creer_grille_final(list_var,n):
    '''
    Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille (en fonction des valeurs logiques prises par les variables de list_var) en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''

def afficher_grille(grille,n):
    ''''''

def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    '''
    


def init_list_var(list_grille_complete,n):
    '''
    Renvoie : une liste list_var initialisant une valuation tenant compte des valeurs non nulles déjà renseignées dans list_grille_complete
'''

'''#test evaluer_clause
#Arg Cas 1 :
clause1=[1,-2,3,-4]
list_var1=[True,True,False,None]
#Renvoi Cas 1: True
#Arg Cas 2 :
clause2=[1,-2,3,-4]
list_var2=[False,True,False,None]
print("renvoi cas 2 : ",evaluer_clause(clause2,list_var2))
#Renvoi Cas 2: None
#Arg Cas 3 :
clause3=[1,-2,3,-4]
list_var3=[None,True,False,True]
#Renvoi Cas 3: False
#Arg Cas 4 :
clause4=[1,-3]
list_var4=[False,False,True]
#Renvoi Cas 4: False
#Arg Cas 5 :
clause5=[]
list_var5=[False,False,True]
#Renvoi Cas 5: False

'''

'''#test enlever_litt_for
for=[[1,-2,3],[2,-3],[-1]]
print(enlever_litt_for(fofor,1))'''

'''#test evaluer_cnf
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var_for1_test1=[True,False,False,None]
print('test1 : ',evaluer_cnf(for1,list_var_for1_test1))
list_var_for1_test2=[None,False,False,None]
print('test2 : ',evaluer_cnf(for1,list_var_for1_test2))
list_var_for1_test3=[True,False,True,False]
print('test3 : ',evaluer_cnf(for1,list_var_for1_test3))'''

'''#test_determine_valuations
#Arg Cas 1:
list_var1=[True,None,False,None]
#Renvoi Cas 1 : [[True, False, False, False], [True, False, False, True], [True, True, False, False], [True, True, False, True]]
#Arg Cas 2:
list_var2=[None,True,None,False,None]
#Renvoi Cas 2: [[True, True, True, False, True], [False, True, True, False, True], [True, True, False, False, True], [False, True, False, False, True], [True, True, True, False, False], [False, True, True, False, False], [True, True, False, False, False], [False, True, False, False, False]]
'''

'''# test retour(list_var,list_chgmts)
#Arg Cas 1 :
list_var1= [False, False, True, True, None] 
list_chgmts1= [[0, False], [1, False], [2, True], [3, True]]
#Renvoi Cas 1
list_var=[False, False, True, False, None]
list_chgmts=[[0, False], [1, False], [2, True], [3, False]]
#Arg Cas 2 :
list_var2= [False, False, True, False, False] 
list_chgmts2= [[0, False], [1, False], [2, True], [3, False], [4, False]]
#Renvoi Cas 2 :
list_var=[False, False, False, None, None]
list_chgmts=[[0, False], [1, False], [2, False]]
'''

'''#test resol_sat_force_brute
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1],[-1,2,3]]
list_var_for1=[None,None,None,None]
boo1,resul1=resol_sat_force_brute(for1,list_var_for1)
print('boo1=',boo1)
print('resul1=',resul1)


for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
boo2,resul2=resol_sat_force_brute(for2,list_var_for2)
print('boo2=',boo2)
print('resul2=',resul2)


for3=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var_for3=[None,None,None,None]
boo3,resul3=resol_sat_force_brute(for3,list_var_for3)
print('boo3=',boo3)
print('resul3=',resul3)
'''

'''#test ultim_resol
for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
boo_for2,lilifor2=ultim_resol(for2,list_var_for2)
print('boo_for2 : ',boo_for2)
print('lilifor2 : ',lilifor2)'''


'''#test for_conj_sudoku
#Cas grille Taille 2
formul_sudok2=for_conj_sudoku(2)
print("formul_sudok taille 2: \n",formul_sudok2)

#Cas grille Taille 3
formul_sudok3=for_conj_sudoku(3)
print("formul_sudok taille 3: \n",formul_sudok3)'''

'''test creer_grille_init & init_list_var cas2
list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
grille2=creer_grille_init(list_grille2,2)
list_var_grille2=init_list_var(grille2,2)
'''

'''#test ultim_resol_simpl_for
#Cas grille Taille 2
formul_sudok2=for_conj_sudoku(2)
list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
list_grille2_f=[[1,2,4],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
grille2=creer_grille_init(list_grille2,2)
afficher_grille(grille2,2)
list_var_grille2=init_list_var(grille2,2)
boo_2,lili2=ultim_resol_simpl_for(formul_sudok2,list_var_grille2)
#corrigé lili2=[False, False, True, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, True]
if boo_2:
    afficher_grille(creer_grille_final(lili2,2),2)
grille2f=creer_grille_init(list_grille2_f,2)
afficher_grille(grille2f,2)
list_var_grille2f=init_list_var(grille2f,2)
boo_2f,lili2f=ultim_resol_simpl_for(formul_sudok2,list_var_grille2f)
if boo_2f:
    afficher_grille(creer_grille_final(lili2f,2),2)'''


'''#test ultim_resol_simpl_for
#Cas grille Taille 3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille1=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)
'''



'''#test ultim_resol_simpl_for_dpll cas3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille3=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for_dpll(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)'''




