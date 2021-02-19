import numpy as np

def exact_score(pizzas, deliveries):

    solve = 0.

    for d in deliveries:

        ingredients = np.array(np.concatenate([pizzas[i].ingredients for i in d[1]]))
        ingredients = np.unique(ingredients)

        solve += len(ingredients)**2

    return solve
