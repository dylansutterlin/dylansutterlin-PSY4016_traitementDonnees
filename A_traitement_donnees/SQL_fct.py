
import pandas as pd
data_frame = pd.read_csv(r'data_base_ACE_erreurs2.csv')


def convert_SQL(data_frame):
        import seaborn as sns
        import pandas as pd
        import matplotlib
        import sqlite3
        from matplotlib import pyplot as plt

        etape = 2
        afficheur = lambda x: str(x)

        conn = sqlite3.connect('data_frame')
        c = conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS STRESS_data (UID,Age,IMC,Origine,Sex,AUCiTSST,RSE_Sum,BDI_Sum,ACEsum)')
        conn.commit()
        sql_query = pd.read_sql_query ('''
                                    SELECT
                                    *
                                    FROM STRESS_data
                                    ''', conn)




