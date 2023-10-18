import pickle
import numpy as np


with open(r"C:\Users\danko\Desktop\books\model.pkl", "rb") as f:
    cs = pickle.load(f)
scores = list(enumerate(cs[1978]))
sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)
sorted_scores = sorted_scores[1:6]

print(sorted_scores)

# j=0n
# print('5 recommandation de la categorie sont :')
# for item in sorted_scores:
#     book_title = 'Fantastic Beasts and Where to Find Them'
#     book_cat =  'Childrens-Books'
#     print(j+1, book_title,'de la categorie :', book_cat)
#     j = j+1
#     if j>=6:
#         break