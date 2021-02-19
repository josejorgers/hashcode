import numpy as np

def build_sol(pizza_index, teams, pizzas):

    pi = 0

    pizza_n = len(pizza_index)
    team_n = len(teams)

    sol = []
    
    score = 0
    for t in range(team_n):
        if pi + teams[t] <= pizza_n:
            
            delivery = [pizza_index[i] for i in range(pi, pi + teams[t])]
            
            value = np.array([pizzas[i].ingredients for i in delivery])
            value = value.sum(axis=0)
            value = np.where(value <= 1, value, 1)
            value = value.sum() ** 2

            score += value

            sol.append((teams[t], delivery))
            pi += teams[t]

    return sol, score


def random_search_solution(pizzas, teams_2, teams_3, teams_4, iterations=100):

    teams = np.random.permutation(([2]*teams_2) + ([3]*teams_3) + ([4]*teams_4))
    pizza_index = np.random.permutation(list([i for i, _ in enumerate(pizzas)]))

    sol, score = build_sol(pizza_index, teams, pizzas)

    for _ in range(iterations):

        coin = np.random.uniform()

        if coin <= .5:
            teams = np.random.permutation(teams)
        else:
            pizza_index = np.random.permutation(pizza_index)

        aux_sol, aux_score = build_sol(pizza_index, teams, pizzas)

        if aux_score > score:
            score = aux_score
            sol = aux_sol

    return sol, score
    


