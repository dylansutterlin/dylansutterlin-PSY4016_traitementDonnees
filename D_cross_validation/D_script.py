
def courbeROC():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import sklearn
    from sklearn import preprocessing
    from sklearn.preprocessing import LabelEncoder
    import sklearn.model_selection
    import sklearn.svm
    import sklearn.metrics
    X_data = pd.read_csv('data_base_ACE_erreurs2.csv')

    #Création d'une variable catégorielle pour le cortisol
    X_data['cortisol_categ'] = X_data['AUCiTSST']

    mean_cort = X_data['AUCiTSST'].mean()

    #Boucle pour couper les valeurs de cortisol en deux groupes
    for index in range(0, len(X_data.AUCiTSST)):
        value = X_data['cortisol_categ'][index]
        if value <= mean_cort :
            X_data['cortisol_categ'][index] = 0 #Non-stressé

        if value > mean_cort :
            X_data['cortisol_categ'][index] = 1 #stressé

    X_data['cortisol_categ']

    #Sauvegarder une copie de la base de données
    X_data = X_data.copy()
    X_data.to_csv('data_base_ACE_erreurs3.csv')

    #Création d'une variable qui contient une liste des données catgorielle
    ls_cortisol_categ = X_data.cortisol_categ.to_list()

    #Transformation des valeurs de la liste
    le = LabelEncoder()
    label=le.fit_transform(ls_cortisol_categ)


    #Création du tableau contenant les caractéristiques
    X_df = X_data.drop(['AUCiTSST','cortisol_categ'], axis=1)


    X = X_df.values
    y = label

    X, y = X[y != 2], y[y != 2]

    n_samples, n_features = X.shape
    random_state = np.random.RandomState(0)
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]


    cv = sklearn.model_selection.StratifiedKFold(n_splits=5)
    classifier = sklearn.svm.SVC(kernel='linear', probability=True,
                     random_state=random_state)

    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)

    # Tracer les courbes ROC
    fig, ax = plt.subplots()
    for i, (train, test) in enumerate(cv.split(X, y)):
        classifier.fit(X[train], y[train])
        viz = sklearn.metrics.plot_roc_curve(
                            classifier, X[test], y[test],
                             name='ROC fold {}'.format(i),
                             alpha=0.3, lw=1, ax=ax)
        interp_tpr = np.interp(mean_fpr, viz.fpr, viz.tpr)
        interp_tpr[0] = 0.0
        tprs.append(interp_tpr)
        aucs.append(viz.roc_auc)


    ax.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
            label='Chance', alpha=.8)

    #Courbe bleu foncé : moyenne des 6 prédictions
    mean_fpr = np.linspace(0, 1, 100)
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = sklearn.metrics.auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)

    ax.plot(mean_fpr, mean_tpr, color='b',
            label=r'ROC moyen (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
            lw=2, alpha=.8)

    #Ajustement des paramètres de l'axe
    ax.set(xlim=[-0.05, 1.05], ylim=[-0.05, 1.05],
           title="Caractéristiques permettant de prédire le stress")
    ax.legend(loc="lower right")
    plt.show()


courbeROC()
