def AA_non_supervisé_PCA():

    import pandas as pd
    import matplotlib.pyplot as plt
    import sklearn
    from sklearn import preprocessing
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    #Importer les données et définir les variable des étiquettes (x)
    #et y pour la variable sur laquelle faire la prédiction
    X_data = pd.read_csv('data_base_ACE_erreurs3.csv')
    X = X_data[['RSE_Sum', 'Sex', 'ACEsum', 'Sex']]
    Y = X_data[['cortisol_categ']]
    x = StandardScaler().fit_transform(X)

    print(X_data.head())

    pca = sklearn.decomposition.PCA(n_components=4)
    pca.fit(X)

    #Composantes de la PCA et la variance expliquée
    print(pca.components_)
    print(pca.explained_variance_)



    #Stocker les composantes dans le dataframe pour ensuite faire une copie du df
    composantes_col = pca.transform(X)
    X_data['_PCA_comp1'] = composantes_col[:, 0]
    X_data['_PCA_comp2'] = composantes_col[:, 1]
    X_data['_PCA_comp3'] = composantes_col[:, 2]
    X_data['_PCA_comp4'] = composantes_col[:, 3]

    #Sauvegarde de la nouvelle base de données
    X_data_copy = X_data.copy()
    X_data_copy.to_csv('data_base_ACE_erreurs4.csv')

    import seaborn as sns
    sns.lmplot(x = "_PCA_comp1", y = "_PCA_comp2", hue='cortisol_categ', data=X_data, fit_reg=False);
    plt.show()


    #Impression de la courbe ROC pour la PCA
    import numpy as np
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('nombre de composants')
    plt.ylabel('variance expliquée cumulative');
    plt.show()


