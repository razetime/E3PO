import json
import sys

alpha = 0.006
beta = 10
w1 = 0.09    
w2 = 0.000015
w3 = 0.000334

with open(f'e3po/result/{sys.argv[1]}/evaluation.json') as f:
    j = json.load(f)

c=json.loads(j[-1]['Cost'])
mse=float(j[-1]['AVG MSE'])
S=1/(alpha*mse+beta*(w1*c[0]+w2*c[1]+w3*c[2]))
print("S =",S)