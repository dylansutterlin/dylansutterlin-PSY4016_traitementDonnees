
import pandas as pd
data_frame = pd.read_excel(r'data_base_ACE_erreurs.xlsx')
data_frame.to_csv()
def data(data_frame):

    #Faire un back up du df1
    df_copy = data_frame.copy(deep = True)

    #Extraction d'un dataframe avec les colonnes qui nous intéresse
    #Voir la descritpions des variables dans le fichier txt
    df1 = df_copy[['UID','Age', 'IMC', 'Origine', 'Sex', 'AUCiTSST', 'RSE_Sum', 'BDI_Sum', 'ACEsum']]

    #Importer les variable sous forme de liste pour y faire référence dans les prochaines étapes
    columns = df1.columns.values.tolist()

    # Nommer les colonnes
    ID = 'UID'
    Age = 'Age'
    IMC = 'IMC'
    ethnie = 'Origine'
    Estime = 'RSE_Sum'
    Cort_reactif = 'AUCiTSST'
    depression = 'BDI_Sum'
    Sex = 'Sex'
    #EA pour Expériences Adverses
    EA = 'ACEsum'

    # Nombre de participants dans la base de données
    print(len(df1)," est le nombre de participants dans la base de données ")


    # Modification des étiquettes de la variable Sex ( "M" = Homme (1); "F" = Femme (0))
    for value in df1['Sex'] :
        if value == "M":
            df1.replace(value, int(str(1)), inplace = True)

            if value == "F":
                df1.replace(value, int(str(0)), inplace = True)


    #Boucle qui permet de supprimer les caratères comme des lettres qui se seraient insérées dans des cellules int/float
    #E.g. s'il y a 32yo, elle va être changé pour 32
    for col in columns:

        for index in range(len(df1)):

            for i in [df1[col][index]]:
                    cell =  i

                    if type(cell) is str:
                        temp = cell
                        #Permet de retirer les lettres dans un string
                        for position in cell:

                            if position.isdigit() is False:
                                cell = cell.replace(position, '')
                        #Option de voir la cellule qui a été changée
                        #print(f'La cellule à la colonne {col} et à la ligne {index} était {temp} mais a été changée pour {cell} ' )

                    df1.replace(i, cell, inplace = True)

    # Modifications du type de valeurs pour l'ensemble des données
    for col in df1.columns:


            if ID in col:
                df1[ID] = df1[ID].astype(float)
            if IMC in col:
                df1[IMC] = df1[IMC].astype(float)
            if Age in col:
                df1[Age] = df1[Age].astype(int)
            if ethnie in col:
                df1[ethnie] = df1[ethnie].astype(str)
            if Estime in col:
                df1[Estime] = df1[Estime].astype(float)
            if Cort_reactif in col:
                df1[Cort_reactif] = df1[Cort_reactif].astype(float)
            if depression in col:
                df1[depression] = df1[depression].astype(float)
            if EA in col:
                df1[EA] = df1[EA].astype(float)

    print(df1.head())
    #voir le type de données pour chaque colonne
    #puis uniformiser les valeurs manquantes pour qu'elles soient toutes NaN
    #Cela permettra par la suite de remplacer ces valeurs par e.g. la moyenne ou la médiane de la colonne
    for col in columns:

        type_cell = df1[col].dtype

        for index in range(0, len(df1)):
            prev_value = df1[col][index]
            valeur = df1[col][index]
            if valeur == ' 'or valeur == '#NULL!' or valeur == 'NaN':
                df1[col][index] = valeur.replace(valeur, 'nan')
                #Option de voir les cellules qui ont été modifiées lors de la boucle
                #print(f'la valeur à la position {col} {index} était {prev_value} a été modifiée pour {df1[col][index]}')


    # Modification des valeurs manquantes par float(NaN)
    df1 = df1.mask(df1 == 'nan')


    ##VALEURS MANQUANTES
    #Vérifier si des colonnes contiennent ds valeurs manquantes
    for col in columns:
        #print(col)
        bool = df1[col].isnull().values.any()

        if bool == True:
            print(f'La colonne {col} contient au moins une valeur manquante')

    # Modification des valeurs manquantes pour la moyenne des scores
    import numpy as np
    import sklearn
    from sklearn import impute
    imp = sklearn.impute.SimpleImputer(missing_values = np.nan, strategy = "mean")

    for col in [Estime, depression, Cort_reactif, EA, IMC]:

        for index in range(len(df1)):

            for i in [df1[col][index]]:
                    cell =  i
                    imp.fit(df1[[col]])
                    df1[col] = imp.transform(df1[[col]])

    print('Le nettoyage est fini !')

    #Enregistrer la copie du data_frame pour l'utiliser dans les prochains scripts
    df2 = df1.copy(deep = True)
    df2.to_csv('data_base_ACE_erreurs2.csv')

    print(df2.head())

data(data_frame)

