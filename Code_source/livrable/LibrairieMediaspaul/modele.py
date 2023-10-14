import pickle
import numpy as np


def modele():
    with open(r"C:\Users\danko\Desktop\books\model.pkl", "rb") as f:
        cs = pickle.load(f)
    scores = list(enumerate(cs[book]))
    sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)

    return sorted_scores

m = modele()
print (m)