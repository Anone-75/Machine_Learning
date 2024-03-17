import pandas as pd

data = pd.read_csv('enjoysport.csv').values
concepts, target = data[:, :-1], data[:, -1]

def train(con, tar):
    specific_h = [con[i] for i, val in enumerate(tar) if val == 'yes'][0]
    for i, val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
    return specific_h

print(train(concepts, target))
