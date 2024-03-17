import numpy as np
import pandas as pd

data = pd.read_csv('enjoysport.csv')
concepts, target = np.array(data.iloc[:, :-1]), np.array(data.iloc[:, -1])

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in specific_h] for _ in specific_h]

    for h, t in zip(concepts, target):
        for x in range(len(specific_h)):
            if t == "yes" and h[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'
            elif t == "no" and h[x] != specific_h[x]:
                general_h[x][x] = specific_h[x] if general_h[x][x] != specific_h[x] else '?'

    return specific_h, [g for g in general_h if g != ['?' for _ in specific_h]]

s_final, g_final = learn(concepts, target)
print("Final Specific_h:", s_final)
print("Final General_h:", g_final)
