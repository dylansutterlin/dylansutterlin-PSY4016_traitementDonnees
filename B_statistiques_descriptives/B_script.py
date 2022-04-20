class stats_frequencielles:


    def hist_estime(hist):
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Histogramme : distribution des scores au questionnaire d'estime de soi
        plt.hist(df.RSE_Sum, bins=15, alpha=0.7,
                color='steelblue', edgecolor='b')

        plt.title("Histogramme de la distribution de l'estime de soi ", fontsize=14)
        plt.xlabel("Score au Rosenberg Self-Esteem Scale", fontsize=14)
        plt.ylabel("Fréquence (%)", fontsize=10)
        plt.show()


    def hist_depression(hist):
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Histogramme : distribution des scores au questionnaire de burnout
        plt.hist(df.BDI_Sum, bins=10, alpha=0.7,
                color='steelblue', edgecolor='b')

        plt.title("Histogramme du score à l'inventaire de dépression de Beck ", fontsize=14)
        plt.xlabel("score à l'inventaire de dépression de Beck", fontsize=14)
        plt.ylabel("Fréquence (%)", fontsize=14)
        plt.show()


    def hist_reactif(hist):
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Histogramme : distribution de l'intensité des variations de cortisol réactif
        plt.hist(df.AUCiTSST, bins=20, alpha=0.7,
                 color='steelblue', edgecolor='b')

        plt.title("Histogramme de la distribution des niveaux de cortisol réactif ", fontsize=14)
        plt.xlabel("Niveaux de cortisol réactif (AUCi)", fontsize=14)
        plt.ylabel("Fréquence (%)", fontsize=14)
        plt.show()


    def hist_EA(hist):
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Histogramme : distribution des variations de cortisol basal au fil du temps
        plt.hist(df.ACEsum, bins=20, alpha=0.7,
                 color='steelblue', edgecolor='b')

        plt.title("Histogramme de la distribution des types différent d'expériences adverses vécus ", fontsize=14)
        plt.xlabel("ypes différent d'expériences adverses vécus", fontsize=14)
        plt.ylabel("Fréquence (%)", fontsize=14)
        plt.show()

    def stats_descriptive(hist):

        import pandas as pd
        df = pd.read_csv('data_base_ACE_erreurs2.csv')

        #Vérification des statistiques descriptives
        print(df.describe())

        #Vérification de la kurtosis
        print(df.kurtosis())

        #Vérification de la skewness
        print(df.skew())
