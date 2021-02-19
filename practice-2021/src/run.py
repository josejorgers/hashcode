from read_write import load_data, output_data
from solutions import random_search_solution

def run(input_dataset, output_file):
    pizzas, t2, t3, t4 = load_data(input_dataset)


    deliveries, score = random_search_solution(pizzas, t2, t3, t4, 500)

    print(score)

    output_data(output_file, deliveries)

if __name__ == '__main__':
    import sys

    args = sys.argv

    input_data = args[1]
    output_file = args[2]

    run(input_data, output_file)