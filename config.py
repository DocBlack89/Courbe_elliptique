import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import ecc





###### Création de la courbe elliptiques #####
A = 109454571331697278617670725030735128145969349647868738157201323556196022393856
B = 107744541122042688792155207242782455150382764043089114141096634497567301547839


##### Ordre de la courbe elliptique ####
l = 109454571331697278617670725030735128146004546811402412653072203207726079563233
N = 109454571331697278617670725030735128145969349647868738157201323556196022393859

##### n pour la multiplication ####
n = 2

##### Point de la courbe elliptique #####
P = ecc.Point(82638672503301278923015998535776227331280144783487139112686874194432446389503, 43992510890276411535679659957604584722077886330284298232193264058442323471611)
Q = ecc.Point(1, 14)

M = ecc.Point(100597391921786027039183722380481804805320476080319934670061678997404767442782,80123073214026054915454326239165515159448240266403681526048086449062769463365)