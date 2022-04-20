class Analyse_stats:

    #Relation entre l'estime de soi et cortisol réactif
    def regression1(reg):
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from statsmodels.formula.api import ols

        X_data = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Régression entre l'estime de soi et les niveaux de cortisol basal
        model = ols("AUCiTSST ~ RSE_Sum + Sex", X_data).fit()
        print(model.summary())

        #Graphique de la relation entre l'estime de soi et cortisol basal
        plt.style.use('seaborn-white')
        fig = sns.lmplot(data = X_data, x = "RSE_Sum", y = "AUCiTSST", line_kws={'color': 'black'})
        plt.scatter(data = X_data, x = "RSE_Sum", y = "AUCiTSST", c = "w", s = 75, edgecolors = "k")
        plt.title("Relation entre l'estime de soi et le cortisol basal chez les travailleurs", fontsize=14)
        plt.xlabel("Estime de soi", fontsize=10)
        plt.ylabel("Niveaux de cortisol réactif", fontsize=10)
        plt.show()


    #Relation entre l'estime de soi et les niveaux de cortisol réactif chez tout les travailleurs
    def regression2(reg):
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from statsmodels.formula.api import ols

        X_data = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Régression entre Estime de Soi et Cortisol réactif chez tout les travailleurs
        model = ols("AUCiTSST ~ ACEsum + Sex", X_data).fit()
        print(model.summary())

        #Graphique de la régression entre le type différent d'expériences adverses et le cortisol réactif
        plt.style.use('seaborn-white')
        fig = sns.lmplot(data =  X_data, x = "ACEsum", y = "AUCiTSST", line_kws={'color': 'black'})
        plt.scatter(data =  X_data, x = "ACEsum", y = "AUCiTSST", c = "w", s = 75, edgecolors = "k")
        plt.title("Relation entre les types différents d'expériences adverses vécu et le cortisol réactif", fontsize=14)
        plt.xlabel("type différent d'expériences adverses", fontsize=10)
        plt.ylabel("cortisol réactif", fontsize=10)
        plt.show()


