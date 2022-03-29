#!/bin/python

'''
define the file_source - the file that includes the columns with the Neuropsychological tests

file_with_zscores - is the file that will have the new zscores
'''

file_source = input('source file (write the complete address of the file that has the columns with the Neuropsychological tests): ')
Age = input('Age column (what is the name of the Age column in the source file?): ')
Edu = input('Education column (what is the name of the Education column in the source file?): ')
file_with_zscores = input('results file (write the complete address of the file with the results, csv type): ')
print(file_source, file_with_zscores)


from os import path, sys
if not path.isfile(file_source):
    print('The file source does NOT exist')
    sys.exit(1)







import pandas as pd
import numpy as np
df = pd.read_csv(file_source)

from lib import all_npsy_tests

def chng_raw_2_zscore(np_Age, np_Edu, Npsy_test, np_test):
    np_ztest = list()
    for val, age, edu in zip(np_test, np_Age, np_Edu):
        function = all_npsy_tests.__function_(Npsy_test)
        mean, std, alert_point = function(int(age), int(edu))
        new_val = (val-mean)/std
        np_ztest.append(new_val)
    return np_ztest

def run_score_conversion_from_db():
    for test in Npsy_norms:
        for age_range in Npsy_norms[test]['Age Edu ranges']:
            a_ranges = Npsy_norms[test]['Age Edu ranges'][age_range]
            if Age >= a_ranges[0] and Age <= a_ranges[1]:
                if Edu <= a_ranges[2]:
                    data = Npsy_norms[test][age_range]['<=']
                else:
                    data = Npsy_norms[test][age_range]['>']
                mean, std, alert = (data['mean'], data['std'], data['alert_point'])
    print(mean, std, alert)

def run_score_conversion():
    print('Reading source file')
    for col_name in df.columns.tolist():
        test_name = all_npsy_tests.__chk_if_test_in_db(col_name)
        if test_name != 'none':
            ls_zscores = chng_raw_2_zscore(df[Age].values, df[Edu].values, test_name, np.array(df[col_name]))
            df[col_name] = ls_zscores
    print('Saving results file')
    df.to_csv(file_with_zscores)

# run_score_conversion()
print('DONE')
