from sklearn import *
#KNN

def AA_supervisé_knn():

    import pandas as pd
    from sklearn.datasets import fetch_lfw_people, make_blobs, make_circles, load_digits
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import GridSearchCV, train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
    from sklearn.svm import SVC         
    from sklearn.decomposition import PCA
    from sklearn.neighbors import KNeighborsClassifier as KNN
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, RandomForestRegressor
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    X_data = pd.read_csv('data_base_ACE_erreurs3.csv')

    
  #Création d'une variable catégorielle avec le cortisol réactif
    mean_cort = X_data['AUCiTSST'].mean()

    #Boucle pour couper les valeurs de cortisol en deux groupes
    for index in range(0, len(X_data.AUCiTSST)):
        value = X_data['AUCiTSST'][index]
        if value < mean_cort :
            X_data['AUCiTSST'][index] = 0 #"Non-stressé"

        if value > mean_cort :
            X_data['AUCiTSST'][index] = 1 #"stressé"

    #Création des prédicteurs (estime de soi, sex et Expériences adverses)
    #et de l'étiquette à prédire, le cortisol (faible ou fort)
    X = X_data[['RSE_Sum', 'Sex', 'ACEsum', 'Age']]
    Y = X_data[['AUCiTSST']]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

    # instantiate learning model (k = 3)
    model = KNN(n_neighbors=3)

    # fitting the model
    model.fit(X_train, y_train)

    # predict the response
    pred = model.predict(X_test)

    # evaluate accuracy
    print(accuracy_score(y_test, pred))

AA_supervisé_knn()




