



# p = [0,0,0,0,1,1,1,1]
# q = [0,0,1,1,0,0,1,1]
# r = [0,1,0,1,0,1,0,1]


# formule = [[1,2,-3],[-1,-2],[1,3]]
# clause = [1,-2,3]
# list_var = [True, None, False]

# # QUESTION 1.3.1 --------------------

# def evaluer_clause(clause,list_var):
#     #Pour chaque valuation on verfie la satisfiabilité de la clause
#     for x,y in zip(clause, list_var):
#         if x >0 and (y == True or y == None):
#             return True
#         elif x<0 and (y == False or y == None):
#             return True
    
#     return False



# # QUESTION 1.3.2 --------------------
# def evaluer_cnf(formule, list_var):
#     list_valuations = []
#     nb_conditions = 0
#     #Pour chaque valuation
#     for val in list_var:
#         nb_conditions = 0
#         #on verifie la satisfiabilité de chaque clause de la formule
#         for clause in formule:
#             if evaluer_clause(clause, val) != False:
#                 nb_conditions += 1
#         if nb_conditions == len(formule):
#             list_valuations.append(val)
#     if len(list_valuations)>0:
#         return True, list_valuations
#     else:
#         return False

    




# # QUESTION 1.4.1 ---------------------

# def determine_valuations(list_var):
#     n = len(list_var)
#     ensemble_valuations = []
#     une_valuation = []
#     valuations_finales = []
    
    
#     for m in range(n):

#         lenght = 2**n
#         changement = lenght / (2**(m+1))
       
#         bit : bool = False
#         une_valuation = []
#         for i in range(lenght):
#             if i%changement == False and i!=False:
#                 bit = not(bit)
#                 une_valuation.extend([bit])
                
#             else:
#                 une_valuation.extend([bit])
#         ensemble_valuations.append(une_valuation)

#     for x in zip(*ensemble_valuations):
        
#         x = list(x)
#         avancement = 0
#         for i in range(len(x)): 
            
#             if (list_var[i]==None):
#                 avancement += 1
               
                
#             elif x[i] == list_var[i]:
#                 avancement +=1
                
                
#         if avancement == len(x):
#             valuations_finales.append(x)
#     return(valuations_finales)
# print(determine_valuations([True,False,None]))
# #Question 1.4.1

# def resol_sat_force_brute(formule, list_var):
#     valuations = determine_valuations(list_var)
    
#     return(evaluer_cnf(formule, valuations))

# print(resol_sat_force_brute(formule, list_var))

def determine_valuations(list_var):
    '''Arguments : une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var
'''
    valuations = []
    none_count = list_var.count(None)
    for i in range(none_count**2):
        val = [True if v is None else v for v in list_var]
        val2 = [ False if v is None else v for v in list_var]
    return val, val2

print(determine_valuations([None, False, None]))