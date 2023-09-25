from os import system
from time import sleep
import numpy as np
from ai import OurNeuralNetwork
from training import generate

console = "clear"

network = OurNeuralNetwork()

def calculation(weight: int, height: int) -> None:
    weight_pounds = int(weight * 2.2)
    height_inch = int(height * 0.39)
    
    weight_ai = weight_pounds - 135
    height_ai = height_inch - 66

    datas = np.array([weight_ai, height_ai])
    result = network.feedforward(datas)

    if float(result) >= 0.951:
        result = str('Ж')
    else:
        result = str('М')
    
    end(result=result)
    
def end(result: str) -> None:
    system(console)
    print(result)
    input("Press to resume...")
    run()


def run() -> None:
    """Start code"""
    system(console)
    weight = input('weight (kg) -> ')
    height = input('height (cm) -> ')
    calculation(weight=int(weight), height=int(height))
    

if __name__ == "__main__":
    system(console)
    print('loading...')
    sleep(1)
    data = generate()[0]
    all_y_trues = generate()[1]
    network.train(data, all_y_trues)
    run()