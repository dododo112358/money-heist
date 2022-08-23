import numpy as np
import random
import networkx as nx
import joblib
import pandas as pd
np.random.seed(100)


def generate_number():
    return "".join(np.random.choice("0 1 2 3 4 5 6 7 8 9".split(), size=8))


group1 = ["9725"+generate_number() for i in range(40)]
group2 = ["9725"+generate_number() for i in range(40)]

calls1 = [np.random.choice(group1, size=2, replace=False) for i in range(850)]
calls2 = [np.random.choice(group1, size=2, replace=False) for i in range(850)]
man_calls1 = [[group1[0], np.random.choice(group1)] for i in range(100)]
man_calls2 = [[group1[0], np.random.choice(group2)] for i in range(100)]

dfs = [pd.DataFrame(lst, columns=["A_PSTN", "B_PSTN"])
       for lst in [calls1, calls2, man_calls1, man_calls2]]
all_calls = pd.concat(dfs, ignore_index=True)
all_calls = all_calls.sample(frac=1).reset_index(drop=True)

joblib.dump(["idan"], "lst.zlib")
G = nx.from_pandas_edgelist(all_calls, source="A_PSTN", target="B_PSTN")

b = nx.betweenness_centrality(G)
print(sorted(b.items(), key=lambda x: x[1], reverse=True))
