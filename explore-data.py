import numpy as np
import pandas as pd
import sys


def getTotalFraudulentTransactions(df: pd.DataFrame):
    sum = df['isFraud'].sum()
    print("Total fraudulent transactions: ", sum)
    return sum

def countUniqueCustomers(df: pd.DataFrame):
    count = df['nameOrig'].nunique()
    print("Total unique Customers", count)

    
def countUniqueRecipients(df: pd.DataFrame):
    count = df['nameDest'].nunique()
    print("Total unique Recipients include Null: ", count)


def main(df: pd.DataFrame):
    print("Start analysing")
    getTotalFraudulentTransactions(df)
    countUniqueCustomers(df)
    countUniqueRecipients(df)
    
if __name__ == '__main__':
    df = pd.read_csv("Fraud.csv", sep=",")
    sys.exit(main(df))
    
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(100,100))
_ = tree.plot_tree(my_tree, 
                   feature_names=my_tree.feature_names_in_.tolist(),  
                   class_names=['0','1'],
                   filled=True)
fig.savefig("decistion_tree.jpg")