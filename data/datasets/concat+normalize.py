import pandas as pd
import os, sys

cwd = os.path.abspath(__file__+"/..")

d1 = pd.read_csv(cwd+"/veritas3.csv")
print("size of veritas3.csv:", len(d1))
d2 = pd.read_csv(cwd+"/pos_samples.csv", sep='\t')
print("size of pos_samples.csv:", len(d2))
d3 = pd.read_csv(cwd+"/good_a3.csv")
print("size of good_a3.csv:", len(d3))

cols = list(set(d1.columns) & set(d2.columns) & set(d3.columns))
print(cols)

d1 = d1.loc[:,cols]
d2 = d2.loc[:,cols]
d3 = d3.loc[:,cols]

c = pd.concat([d2,d3]).sample(frac=1)

#c['verdict'] = c['verdict'].str.lower()

#c.loc[c['verdict'] == "legend", 'verdict'] = 'false'
#c.loc[c['verdict'] == "false.", 'verdict'] = 'false'
#c.loc[c['verdict'] == "mfalse", 'verdict'] = 'false'
#c.loc[c['verdict'] == "mostly false", 'verdict'] = 'mfalse'
#c.loc[c['verdict'] == "true.", 'verdict'] = 'true'
#c.loc[c['verdict'] == "mtrue", 'verdict'] = 'true'
#c.loc[c['verdict'] == "mostly true", 'verdict'] = 'mtrue'

print("size of concatenated \"dataset\":",len(c))
c.to_csv("dataset.csv", index=False, sep=',')
print(c.groupby('verdict').count())
