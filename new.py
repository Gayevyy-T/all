#Deep learning
#data science/big data
#artificial inteligence
#MachineLearning (include pandas ans data analises)

import pandas as pd
import csv
#pd.__version__

#x = pd.read_csv('C:\\Users\\A645674\\Downloads\\Services.csv')
col = ['OS', 'SERVICETYPE','STATE', 'OFFSHORE']

y = pd.read_csv('C:\\Users\\A645674\\Downloads\\Services.csv', usecols = col, decimal = ',')
#or
#x[['OS', 'SERVICETYPE','STATE', 'OFFSHORE']]
#or
#x.loc[:,'OS':'SERVICETYPE']





=====================================================



y['OS'].tolist() --> sorted coulumn OS into a list
y.to_csv('C:\\Users\\A645674\\Downloads\\new.csv')


#${line[3]}" =~ Windows ]] && [[ "${line[5]}" =~ Application|IIS|TomCat|http ]] 
#&& [[ "${line[9]}" =~ Up|Down ]] && [[ "${line[15]}" =~ (L1\-L2|L3)\ \-\ (ROM|PL) ]]; 
