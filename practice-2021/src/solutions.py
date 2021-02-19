import numpy as np
from scores import exact_score

def build_sol(pizza_index, teams):

    pi, ti = 0, 0

    pizza_n = len(pizza_index)
    team_n = len(teams)

    sol = []
    
    for t in range(team_n):
        if pi + teams[t] <= pizza_n:
            sol.append((teams[t], [pizza_index[i] for i in range(pi, pi + teams[t])]))
            pi += teams[t]

    return sol
            

# def exact_solution(pizzas, teams_2, teams_3, teams_4):

#     pizzas_left = len(pizzas)



def random_search_solution(pizzas, teams_2, teams_3, teams_4, iterations=100):

    teams = np.random.permutation(([2]*teams_2) + ([3]*teams_3) + ([4]*teams_4))
    pizza_index = np.random.permutation(list([i for i, _ in enumerate(pizzas)]))

    sol = build_sol(pizza_index, teams)

    score = exact_score(pizzas, sol)

    for _ in range(iterations):

        teams = np.random.permutation(teams)
        pizza_index = np.random.permutation(pizza_index)

        aux_sol = build_sol(pizza_index, teams)

        aux_score = exact_score(pizzas, aux_sol)

        if aux_score > score:
            score = aux_score
            sol = aux_sol

    return sol, score
    


