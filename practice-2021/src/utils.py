import numpy as np
from sklearn.preprocessing import OneHotEncoder

def from_pizzas_to_encoded_pizzas(pizzas):

    all_ingredients = []

    for p in pizzas:
        all_ingredients += p.ingredients

    ing_matrix = np.array(all_ingredients).reshape(-1, 1)
    
    ohe = OneHotEncoder()
    ohe.fit(ing_matrix)

    for i in range(len(pizzas)):

        ing_matrix = ohe.transform(np.array(pizzas[i].ingredients).reshape(-1,1))
        pizzas[i].ingredients = ing_matrix.sum(axis=0)
        