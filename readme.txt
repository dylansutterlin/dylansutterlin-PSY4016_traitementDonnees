Projet s'intéressant au lien entre le stress, l'estime de soi et les expériences adverses

DESCRIPTION PROJET
Les données utilisées dans ce projet proviennent d’une étude de Raymond et collaborateurs, (2021), qui s’est intéressé à la relation entre l’Adversité précoce (AP) – des expérience(s) adverse(s) vécues pendant l’enfance comme la pauvreté ou la maltraitance – et la réponse de stress. Les variables principales sont des mesures d’AP, soit 1) L’âge de la première exposition à l’expérience adverse, 2) Le nombre de types d’expériences adverses vécues dans l’enfance (échelle nominale de 0-13 – score déterminé par un questionnaire) et 3) Des mesures de cortisol (la principale hormone de stress) à plusieurs temps lors d’une tâche visant à stresser des participants. Faisant partie d’un projet doctoral plus vaste, la base de données comporte également d’autres variables, dont une mesure d’estime de soi. 
Les variables numériques (échelles à intervalles et continues):
•	L’âge de la première exposition à l’expérience adverse
•	Le nombre de types d’expériences adverses vécues dans l’enfance (0-13)
•	L’estime de soi 
•	Concentration salivaire de cortisol à plusieurs temps 
•	Âge

Les variables nominales et catégorielles :
•	Sexe

Variables et hypothèses
1)	La littérature suggère est qu’il existe un lien entre l’estime de soi et la réponse de stress. On émet donc l’hypothèse que la concentration de cortisol (suite à une tâche stressante) sera modulée par le score à une échelle d’estime de soi, de telle sorte qu’une plus haute estime de soi prédira une réponse de stress moindre au moment où la concentration de cortisol est maximal.

Variable x : score d’estime de soi
Variable y : Concentration salivaire de cortisol(microgramme/mol)


2)	Les études montrent que l’adversité vécues dans l’enfance est liée à une réponse de stress altérée à l’âge adulte. La direction de cette influence n’est toutefois pas claire. L’hypothèse est que plus le type différent d’expériences adverses vécues augmente (e.g. maltraitance + pauvreté + intimidation = 3 types différents versus 1 seul type), plus la concentration de cortisol sera maximale suite à une tâche stressante. 

Variable x : nombre de types différents d’adversité vécus
Variable y : Concentration salivaire de cortisol(microgramme/mol)


DSECRIPTION DU SCRIPT
1. Descriptions des variables

'UID' : Id. du participants
'Age' : Âge
'IMC' : Indice de masse corporelle, on sait qu'il existe une association positive entre l'IMC et les 
	Hornmones de stress.
'Origine' : Ethnicité
'AUCiTSST': Aire sous la courbe du cortisol réactif pendant une tâche stressante en laboratoire (le Trier
            social Stress Test -TSST)
'Sex'
'RSE_Sum' : Score total à l'échelle d'estime de soi de Rosenberg
'BDI_Sum' : Score total à l'inventaire de Dépression de Beck
'ACE_Sum' : Score total au questionnaire d'expériences adverses

A. Prétraitement des données

Seules les colonnes pertinentes ont été sélectionnées pour la suite du pipeline. Les données ont été nettoyées, c'est-à-dire que si une cellule devait être un float et qu'elle contenait des lettres, ces dernières ont été retirées. Ensuite, Les valeurs manquantes ont été uniformisées (certaines cellules vides avait #NULL!, d'autres NaN et d'autres étaient simplement vides). Ensuite, les valeurs NaN ont été remplacées par la moyenne de la colonne.

La base de données modifiée a été enregistrée sous le nom de data_base_ACE_erreurs2.csv

B. Statistiques descriptives

Premièrement, quatre histogrammes ont été fait afin d'analyser visuellement les données. L'estime de soi, les expériences adverses et le cortisol semble être distribués assez normalement, mais ce n'est pas le cas pour les score de symptôme dépressif. La variable dépression ne sera pas utilisée dans les analyses futures. Elle servait seulement à titre de description de l'échantillon. On voit dans l'histogramme que les participants ont des scores dépressifs globalement assez faibles.

Ensuite, les statistiques descriptives ont été sorties, ainsi que la kurtose et l'applatissement pour chaque variable. Les valeurs confirment l'intuition visuelle, soit que la variable de dépression n'est pas distribuée normalement, mais également que la variable d'Expériences adverses est très applatie.

C. Analyses statistiques

Les hypothèses étaient que l'estime de soi serait un bon prédicteur du cortisol réactif, en contrôlant pour le sex. On se serait attendu à une association négative entre les deux variables. La régression et le graphique (nuage de points) suggèrent que ces deux variables ne sont pas liées (Béta = -0.0896, P = ,295). On obtient des résultat similaire pour ce qui est de l'association entre le nombre d'expériences adverses différent qu'une personne a vécu et le cortisol réactif, en contrôlant pour le sex (Béta = -0.0064, p = ,316).

D. Procédure de validation croisée et courbe ROC

Dans ce script, une procédure de validation croisée est initialisée.La courbe ROC est représenté graphiquement afin de voir le pouvoir prédictif du modèle en ce qui a trait à la prédiction de la réponse de stress (cortisol réactif).

E. Apprentissage automatique supervisé

L'algorithme KNN est implémenté. Les variables sex, 