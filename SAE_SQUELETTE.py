from re import X
import numpy as np
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

def test_for(mess,formu,res_for):
    res=True
    for el1 in formu:
        for el2 in res_for:
            res=(set(el1)==set(el2))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    for el2 in res_for:
        for el1 in formu:
            res=(set(el2)==set(el1))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    res=False
    for i in range(len(formu)-1):
        for el in formu[i+1:]:
            if set(formu[i])==set(el):
                print(mess+'wowowow y a du doublon là-dedans')
                return 
    print(mess+'Ok')

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
    indices = [i for i in range(len(list_var)) if list_var[i] == None]
    for i in range(2**len(indices)):
        valuation = copy.deepcopy(list_var)
        for j in range(len(indices)):
            valuation[indices[j]] = (i // 2**j) % 2 == 1
        valuations.append(valuation)	
    return valuations

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
# for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
# list_var_for1_test1=[True,False,False,None]
# test('test1 resol_sa_force_brut: ',resol_sat_force_brute(for1,list_var_for1_test1),(True, [True,False,False,False]))

def enlever_litt_for(formule,litteral):
    '''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''
    
    for i in range(len(formule)-1,-1,-1):
        for j in range(len(formule[i])):
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
for1=[[1,2],[-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var = [True,None,None,None]


list_var_for1=[False, None, None, False, None]
for1=[[-5, -3, 4, -1], [3], [5, -2], [-2, 1, -4], [1, -3]]
cor_for1=[[3], [5, -2], [-3]]
test_for('test_init_formule_simpl_for : ',init_formule_simpl_for(for1,list_var_for1),cor_for1)
list_var_for2= [False, True, False, True, False]
for2= [[3, 2, 1], [-1, -2, 5]]
cor_for2=[]
test_for('test_init_formule_simpl_for : ',init_formule_simpl_for(for2,list_var_for2),cor_for2)

list_var_for3= [None, None, None, True, None]
for3= [[-5, -1], [-1, -3], [4], [-4, 1], [-2, -1, 3]]
cor_for3=[[-5, -1], [-1, -3], [1], [-2, -1, 3]]

test_for('test_init_formule_simpl_for : ',init_formule_simpl_for(for3,list_var_for3),cor_for3)




#TEST OK

for1=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt1=4

test('essai cas 1 enlever_litt_for : ',enlever_litt_for(for1,litt1),[[-1, 2, 3], [-1, -2, -5], []])

def retablir_for(formule_init,list_chgmts):
    # Créer une liste des variations
    formule = copy.deepcopy(formule_init)
    list_var = [None for i in range(5)]
    # Ajouter les variations
    for changement in list_chgmts:
        list_var[changement[0]] = changement[1]
    # Simplifier la formule
    formule = init_formule_simpl_for(formule,list_var)

    return formule
# TEST OK

formule_init=  [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]]
list_chgmts1 = [[0, True], [1, True], [2, False]]
form1 = [[-5], [4, 5], [-4, 5]]

list_chgmts2 = [[0, True], [1, True], [2, False], [3, True], [4, False]]
form2 = [[]]

list_chgmts3 = [[0, True], [1, True], [2, False], [3, False]]
form3 = [[-5], [5]]
test('essai cas 1 retablir_for : ',retablir_for(formule_init,list_chgmts1),form1)
test('essai cas 2 retablir_for : ',retablir_for(formule_init,list_chgmts2),form2)
test('essai cas 3 retablir_for : ',retablir_for(formule_init,list_chgmts3),form3)



def progress(list_var,list_chgmts):
    '''
Arguments : list_var, list_chgmts définies comme précédemment
    Renvoie : l1,l2
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts
     
'''
    l1 = list_var

    l2 = list_chgmts
    for i in range(len(l1)):
        if l1[i] == None:
            l1[i] = True
            l2.append([i,True])
            
            return l1,l2

    return l1,l2
# TEST OK
'''
list_var=[True, None, None, None, None]
list_chgmts=[[0, True]]
l1=[True, True, None, None, None]
l2=[[0, True], [1, True]]
test("essai cas 1 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[0, True], [1, False], [2, False]]
l1=[True, False, False, True, None]
l2=[[0, True], [1, False], [2, False], [3, True]]
test("essai cas 2 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[None, None, None, None, None]
list_chgmts=[]
l1=[True, None, None, None, None]
l2=[[0, True]]
test("essai cas 3 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[False, None, None, None, None]
list_chgmts=[[0, False]]
l1=[False, True, None, None, None]
l2=[[0, False], [1, True]]
test("essai cas 4 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, None, None, None]
list_chgmts=[]
l1=[True, False, True, None, None]
l2=[[2, True]]
test("essai cas 5 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[2, False]]
l1=[True, False, False, True, None]
l2=[[2, False], [3, True]]
test("essai cas 6 progress : ",progress(list_var,list_chgmts),(l1,l2))

'''

def retablir_for(formule_init,list_chgmts):
    '''Arguments : une formule initiale et une liste de changements à apporter sur un ensemble de variables (chaque changement étant une liste [i,bool] avec i l'index qu'occupe la variable dans list_var et
     bool la valeur logique qui doit lui être assignée) 
    Renvoie : la formule simplifiée en tenant compte de l'ensemble des changements
'''
    formule_simpl = formule_init
    for i in list_chgmts:
        if i[1] :
            formule_simpl = enlever_litt_for(formule_simpl,i[0]+1)
        elif i[1] == False :
            formule_simpl = enlever_litt_for(formule_simpl,-(i[0]+1))
    return formule_simpl

# TEST OK
'''
formule_init=  [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]]
list_chgmts1 = [[0, True], [1, True], [2, False]]
form1 = [[-5], [4, 5], [-4, 5]]

list_chgmts2 = [[0, True], [1, True], [2, False], [3, True], [4, False]]
form2 = [[]]

list_chgmts3 = [[0, True], [1, True], [2, False], [3, False]]
form3 = [[-5], [5]]
test('essai cas 1 retablir_for : ',retablir_for(formule_init,list_chgmts1),form1)
test('essai cas 2 retablir_for : ',retablir_for(formule_init,list_chgmts2),form2)
test('essai cas 3 retablir_for : ',retablir_for(formule_init,list_chgmts3),form3)'''

def progress_simpl_for(formule,list_var,list_chgmts):
    '''Arguments : formule,list_var, list_chgmts définies comme précédemment
    Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
    Une fonction progress_simpl_for(formule,list_var,list_chgmts) qui permet de des-
    cendre dans l’arbre jusqu’à un premier changement à apporter à la liste de variables. La
    fonction renvoie alors la formule logique simplifiée, la nouvelle valuation en cours list_var
    et la nouvelle liste des changements apportés à list_var depuis le lancement de la résolu-
    tion de la formule (précisions dans la description de progress(list_var,list_chgmts)) ;
'''
    l1,l2 = progress(list_var,list_chgmts)
    form = retablir_for(formule,l2)
    return form,l1,l2   
    


# formule= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
# list_var= [None, None, None, None, None] 
# list_chgmts= []
# cor_form,cor_l1,cor_l2= ([[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]],[True, None, None, None, None],[[0, True]])
# test('essai1_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))
 
 
# formule= [[-5], [5]] 
# list_var= [True, True, True, False, None] 
# list_chgmts= [[0, True], [1, True], [2, True], [3, False]]
# cor_form,cor_l1,cor_l2= ([[]],[True, True, True, False, True],[[0, True], [1, True], [2, True], [3, False], [4, True]])
# test('essai2_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

# formule= [[3, -4], [-3, 4, 5], [-4, 5]] 
# list_var= [True, False, None, None, None] 
# list_chgmts= [[0, True], [1, False]]
# cor_form,cor_l1,cor_l2= ([[4, 5], [-4, 5]],[True, False, True, None, None],[[0, True], [1, False], [2, True]])
# test('essai3_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

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
    
    Une fonction retour(list_var,list_chgmts) qui va permettre de remonter dans l’arbre
    en annulant les effets des changements précédemment effectués et en supprimant leurs en-
    registrements, jusqu’à arriver à un branchement où on puisse effectuer un nouveau change-
    ment en redescendant vers la droite dans l’arbre, auquel cas on renverra la nouvelle liste des
    valeurs affectées aux variables et la nouvelle liste des changements
    '''
    if len(list_chgmts)>0:
        if list_chgmts[-1][1]==True:
            list_var[list_chgmts[-1][0]]=False
            list_chgmts[-1][1] = False
            
        else:
            list_var[list_chgmts[-1][0]]=None
            list_chgmts = list_chgmts[:-1]
            list_var, list_chgmts = retour(list_var,list_chgmts)
    return list_var,list_chgmts



           
            
            
            
'''
list_var= [True, True, None, None, None]
list_chgmts= [[0, True], [1, True]]
l1= [True, False, None, None, None]
l2= [[0, True], [1, False]]
test("essai cas 1 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, None, None, None]
list_chgmts= [[0, True], [1, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 2 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= []
l1= [True, False, False, True, None]
l2= []

test("essai cas 4 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, True, False, True, None]
list_chgmts= [[1, True]]
l1= [True, False, False, True, None]
l2= [[1, False]]
test("essai cas 5 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= [[1, False]]
l1= [True, None, False, True, None]
l2= []
test("essai cas 6 retour : ",retour(list_var,list_chgmts),(l1,l2))
test("essai cas 3 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, False, False]
list_chgmts= [[0, True], [1, False], [2, False], [3, False], [4, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 4 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, True, False, True, None]
list_chgmts= [[1, True]]
l1= [True, False, False, True, None]
l2= [[1, False]]
test("essai cas 5 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= [[1, False]]
l1= [True, None, False, True, None]
l2= []
test("essai cas 6 retour : ",retour(list_var,list_chgmts),(l1,l2))
'''
    
    
    

def retour_simpl_for(formule_init,list_var,list_chgmts):
    '''
    Une fonction retour_simpl_for(formule_init,list_var,list_chgmts) qui va permettre
    de remonter dans l’arbre en annulant les effets des changements précédemment effectués
    et en supprimant leurs enregistrements, jusqu’à arriver à un branchement où on puisse ef-
    fectuer un nouveau changement en redescendant vers la droite dans l’arbre, auquel cas on
    renverra la nouvelle formule à prendre en compte (établie à partir de la formule initiale dé-
    finie au début de la résolution et de la nouvelle liste des changements à prendre en compte),
    la nouvelle liste des valeurs affectées aux variables, la nouvelle liste des changements en
    cours. Une attention sera à apporter au cas où la liste des changements serait vide.
    Ces précédentes fonction s’appuieront sur les deux fonctions suivantes pour la simplification d’une
    formule logique ou le retour en arrière sur ces simplifications : enlever_litt_for(formule,liste_var) et retablir_for(formule,liste_var)
    
Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    if len(list_chgmts)>0:
        if list_chgmts[-1][1]==True:
            list_var[list_chgmts[-1][0]]=False
            list_chgmts[-1][1] = False
            form = retablir_for(formule_init,list_var)
            
        else:
            list_var[list_chgmts[-1][0]]=None
            list_chgmts = list_chgmts[:-1]
            form = retablir_for(formule_init,list_var)
            list_var, list_chgmts = retour_simpl_for(formule_init,list_var,list_chgmts)
    else:
        form = formule_init
    return form,list_var,list_chgmts

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
          l1 : une liste de valuations rendant la formule vraie ou une liste vide
    Une fonction resol_parcours_arbre(formule_init,list_var,list_chgmts) qui va éva-
    luer la formule donnée initialement avec la liste des valuations en cours et va, en fonction
    du résultat, décider éventuellement de la progression du parcours dans l’arbre ou du re-
    tour sur des hypothèses émises précédemment. Avec une approche récursive elle doit in
    fine renvoyer deux éléments :
    — Un booléen précisant si la formule est satisfiable ou non
    — Une liste         '''



    
    
'''
formule_init= [[1, 4, -5], [-1, -5], [2, -3, 5], [2, -4], [2, 4, 5], [-1, -2], [-1, 2, -3], [-2, 4, -5], [1, -2]] 
list_var= [True, True, False, True, None] 
list_chgmts= [[1, True]]
cor_resol=(False, [])
test('essai1_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
list_var= [True, False, None, False, True] 
list_chgmts= [[0, True]]
cor_resol=(True,[True, False, True, False, True])
test('essai2_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True,[False, True, False, True, False])
test('essai3_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)
'''

def resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts):#la même distinction peut être faite entre formule et formule_init
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
''' 
        
'''
formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
formule= [[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, None, None, None, None] 
list_chgmts= [[0, True]]
cor_resol=(True, [True, False, True, True, True])
test('essai1_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
formule= [[5], [-5]] 
list_var= [False, True, True, False, None] 
list_chgmts= [[2, True]]
cor_resol=(False, [])
test('essai2_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
formule= [[-5], [4]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True, [False, True, False, True, False])
test('essai3_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)
'''

    
    

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
'''Arguments : une liste de listes(contenant les coordonnées à renseigner et le nombre correspondant) et un entier donnant la taille de la grille
Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille en la parcourant ligne après ligne de haut
en bas et de gauche à droite
Créer une fonction creer_grille_init(list_grille_coord_connues,n) prenant en
arguments une liste de listes(contenant les coordonnées des cases renseignées dans la
grille et le nombre correspondant) et un nombre n spécifiant la taille de la grille voulue
et renvoyant une liste à une dimension de taille n*n*n*n  attribuant la valeur 0 à toutes les cases pour lesquelles
la valeur est inconnue et la valeur figurant dans la liste en argument pour les autres.
Ainsi avec [[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]] et n=2 on renverrait la liste :
[0, 1, 0, 0, 4, 2, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0]
'''
def creer_grille_init(list,n):
     # Créer la grille (avec des 0)
    grille = [0 for i in range(n**2**2)]
    # Assigner les valeurs 
    for valeur in list:
        # Numéro de ligne * taille de la ligne + numéro de colonne - 1
        grille[(valeur[0]-1)*(n**2)+(valeur[1]-1)] = valeur[2]
    return grille


# #test creer_grille_init & init_list_var cas2
# list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
# grille2=creer_grille_init(list_grille2,2)
# print(grille2)
# # list_var_grille2=init_list_var(grille2,2)
def creer_grille_final(list_var,n):
    '''
    Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille (en fonction des valeurs logiques prises par les variables de list_var) en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''

def afficher_grille(grille,n):
    '''
    Créer une fonction afficher_grille(list_grille_complete,n) qui, à partir d’une
    liste au format correspondant à une liste renvoyée par la fonction précédente, permettra
    l’affichage de la grille sous sa forme habituelle (on pourra par exemple simplement utiliser
    la fonction reshape de la bibliothèque numpy. Ainsi à partir de l’exemple précédent on
    obtiendrait la grille (la mise en forme avec les lignes n’est pas attendue) '''
    # Afficher la grille
    print(np.reshape(grille, (n**2, n**2)))
# afficher_grille(grille2,2)

def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    Créer une fonction for_conj_sudoku(n) prenant en argument la dimension de la grille
    voulue (nombre de ligne et colonne par région) et renvoyant la formule normale conjonc-
    tive attendue permettant le respect des contraintes 𝐶1 à 𝐶4. Les contraintes 𝐶1 et 𝐶2
    se traduiront chacune par n4 clauses de n2 littéraux (chaque nombre doit être présent au
    moins une fois) et (n4 (n2 −1))/2 clauses binaires (mais pas de doublon). En évitant des doublons
    avec des clauses déjà précédemment établies, la contrainte 𝐶3 se traduira par n4 clauses de
    n2 littéraux et (n4*(n2 −5))/2 clauses binaires. La contrainte 𝐶4 se traduira par (n6*(n2 −1))/2 clauses binaires
       
    '''
    # Créer la formule
    formule = []
    # Ajouter les contraintes C1 et C2
    
    return formule

#Cas grille Taille 3
formul_sudok3=for_conj_sudoku(3)


def init_list_var(list_grille_complete,n):
    '''
    Renvoie : une liste list_var initialisant une valuation tenant compte des valeurs non nulles déjà renseignées dans list_grille_complete 
    Créer une fonction init_list_var(list_grille_complete,n) permettant de renvoyer
    une initialisation de la liste de valuations list_var en tenant compte des valeurs déjà
    renseignées dans list_grille_complete.
    '''
    list_var = []
    for i in range(n**2):
        for j in range(n**2):
            if list_grille_complete[i*n**2+j] != 0:
                list_var.append((i*n**2+j)*n+list_grille_complete[i*n**2+j])
    return list_var

    


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




