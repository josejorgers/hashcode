import os
from models import Pizza

DATA_INPUT_DIR = os.path.join('..', 'data')
DATA_OUTPUT_DIR = os.path.join('..', 'outputs')

def load_data(filename):
    
    with open(os.path.join(DATA_INPUT_DIR, filename)) as file:

        lines = file.readlines()

        str_data = lines[0].split(' ')

        _, teams_2, teams_3, teams_4 = int(str_data[0]), int(str_data[1]), int(str_data[2]), int(str_data[3])

        lines = lines[1:]
        
        pizzas = []
        for i, line in enumerate(lines):

            line = line[:-1]

            str_data = line.split(' ')

            pizzas.append(Pizza(i, str_data[1:]))

        return pizzas, teams_2, teams_3, teams_4


def output_data(filename, deliveries):

    '''
    deliveries: (team_members, [list of pizza indices])
    '''
    
    try:
        file =  open(os.path.join(DATA_OUTPUT_DIR, filename), 'x')
    except:
        file = open(os.path.join(DATA_OUTPUT_DIR, filename), 'w')
        
    n_teams = len(deliveries)
    file.write(f'{n_teams}\n')

    for d in deliveries:
        file.write(f'{d[0]}')
        for pizza in d[1]:
            file.write(f' {pizza}')
        file.write('\n')


if __name__ == '__main__':

    with open(os.path.join(DATA_OUTPUT_DIR, 'c')) as f:
        lines = f.readlines()
        print(len(lines))