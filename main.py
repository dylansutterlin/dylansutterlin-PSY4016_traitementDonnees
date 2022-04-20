import os
import pandas as pd

data_frame = pd.read_excel(r'data_base_ACE_erreurs.xlsx')
data_frame.to_csv()



#A : Traitement des données
#from A_traitement_donnees import script_data

#script_data.data(data_frame)

#B : Statistiques descriptives
from B_statistiques_descriptives import B_script

#Histogrammes
fct_freq = B_script.stats_frequencielles()

fct_freq.hist_estime()

fct_freq.hist_depression()

fct_freq.hist_reactif()

fct_freq.hist_EA()

#Statistiques descriptives
fct_freq.stats_descriptive()

#C : Analyses statistiques, régressions linéaires

from C_Statistiques import C_script

fct_regression = C_script.Analyse_stats()

fct_regression.regression1()

fct_regression.regression2()

#D : Validation croisée et courbe ROC

from D_cross_validation import D_script

D_script.courbeROC()


E : Apprentissage automatique supervisé
