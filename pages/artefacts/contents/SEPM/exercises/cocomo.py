import sys
import math

def do_calculation_and_display_results(kloc, model):
    if model != 'organic' and model != 'semi_detached' and model != 'complex':
        print(f'Unsupported model: {model}')
        return
    
    a = 0
    b = 0
    c = 0
    d = 0

    if model == 'organic':
        a = 2.4
        b = 1.05
        c = 2.5
        d = 0.38
    elif model == 'semi_detached':
        a = 3.0
        b = 1.12
        c = 2.5
        d = 0.35
    else:
        a = 3.6
        b = 1.20
        c = 2.5
        d = 0.32
    
    effort = a * math.pow(kloc, b)
    dtime = c * math.pow(effort, d)
    staff = effort / dtime

    print(f'Estimated result using Cocomo model: {model}')
    print(f'{str(round(effort))} person-months')
    print(f'{str(round(dtime))} months')
    print(f'{str(round(staff))} person')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ')
        print('python3 cocomo.py [KLOC] [model]')
    else:
        kloc = int(sys.argv[1])
        model = sys.argv[2]
        do_calculation_and_display_results(kloc, model)
