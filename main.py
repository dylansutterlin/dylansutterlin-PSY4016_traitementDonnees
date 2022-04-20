import os
import pandas as pd

data_frame = pd.read_excel(r'data_base_ACE_erreurs.xlsx')
data_frame.to_csv()

#PRE : Importer la base de données en format SQL

from A_traitement_donnees import SQL_fct

SQL_fct.convert_SQL(data_frame)

#A : Traitement des données
from A_traitement_donnees import A_script_data

A_script_data.data(data_frame)


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


#D : Apprentissage supervisé, KNN et SVM
#**graphique (courbe ROC) sera imprimée pour SVM

from D_AA_supervisé import D_script

D_script.AA_supervisé_knn()

D_script.SVM()

#E : Apprentissage non-suoervisé, PCA
#**graphique sera imprimé pour PCA

from  E_AA_non_supervisé import E_script

E_script.AA_non_supervisé_PCA()





