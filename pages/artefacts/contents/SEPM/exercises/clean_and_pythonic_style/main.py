'''
The main script of performing estimation using COCOMO model
'''
import sys
import math

def do_calculation_and_display_results(kloc: int, model: str) -> None:
    '''
    Do calculation and display results

    Args:
        kloc: The total number of lines of code
        model: The selected model for calculation

    Returns:
        None
    '''
    if model not in ['organic', 'semi_detached', 'complex']:
        print(f"Unsupported model: {model}")
        return

    model_constant_mapper = {
        'organic': [2.4, 1.05, 2.5, 0.38],
        'semi_detached': [3.0, 1.12, 2.5, 0.35],
        'complex': [3.6, 1.20, 2.5, 0.32],
    }
    model_constants = model_constant_mapper[model]

    effort = model_constants[0] * math.pow(kloc, model_constants[1])
    dtime = model_constants[2] * math.pow(effort, model_constants[3])
    staff = effort / dtime

    print(f"Estimated result using Cocomo model: {model}")
    print(f"{str(round(effort))} person-months")
    print(f"{str(round(dtime))} months")
    print(f"{str(round(staff))} person")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ")
        print("python3 cocomo.py [KLOC] [model]")
    else:
        _kloc = int(sys.argv[1])
        _model = sys.argv[2]
        do_calculation_and_display_results(_kloc, _model)
