from Documentaire1 import Documentaire, Exemplaire 
import copy
doc0 = Documentaire("Brains" ,"3/12/2023")
doc1 = Documentaire("motivation" ,"11/11/2023")
docc = copy.copy (doc0)

print (doc0.ToString())
print(doc1.ToString())
print(doc0.Eqauls(doc1))
print (docc.ToString())

ex2 = Exemplaire("Brains" ,"3/12/2023","3/12/2023")
ex3 = Exemplaire("motivation" ,"11/11/2023","11/11/2023", 46899)

print (ex2.ToString())
print(ex3.ToString())
print(ex2.Eqauls(ex3))