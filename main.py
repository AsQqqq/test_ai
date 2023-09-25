from os import system
from time import sleep
import numpy as np
from ai import OurNeuralNetwork

network = OurNeuralNetwork()

# Определим набор данных
data = np.array([
  [-2, -1],  # Алиса
  [25, 6],   # Боб
  [17, 4],   # Чарли
  [-15, -6], # Диана 
])
all_y_trues = np.array([
  1, # Алиса
  0, # Боб
  0, # Чарли
  1, # Диана
])

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
    system('cls')
    print(result)
    print('loading...')
    sleep(5)
    run()



def run() -> None:
    """Start code"""
    system('cls')
    print('loading...')
    sleep(1.5)
    network.train(data, all_y_trues)
    system('cls')
    weight = input('weight (kg) -> ')
    height = input('height (cm) -> ')
    calculation(weight=int(weight), height=int(height))
    

if __name__ == "__main__":
    run()