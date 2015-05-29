import pandas as pd
import numpy as np
import re




#functions to generate features, take in dataframe and output dataframe of features
def exampleFeature(df):

    return df




inFile = "/Users/mattburg/dssg/project-inspector-gadget/data/Building_Violations_sample.csv"
outFile = "/Users/mattburg/dssg/project-inspector-gadget/data/Building_Violations_sample.csv"

df = pd.read_csv(fileName)


featureFuncs = [exampleFeature]
for featureFunc in featureFuncs:
    features = featureFunc(df)
    df = df.concat([df,features],axis = 1)

df.write_csv(outFile)
