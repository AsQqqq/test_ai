import numpy as np
import random

ars = 100

def generate() -> np.array:
  girl_weight = []
  girl_height = []

  boy_weight = []
  boy_height = []

  for i in range(ars):
    # Женский вес
    number = random.randint(40, 60)
    girl_weight.append(int(number * 2.2) - 135)
  for i in range(ars):
    # Мужский вес
    number = random.randint(60, 110)
    boy_weight.append(int(number * 2.2) - 135)
  for i in range(ars):
    # Женский рост
    number = random.randint(140, 170)
    girl_height.append(int(number * 0.39) - 66)
  for i in range(ars):
    # Мужской рост
    number = random.randint(160, 210)
    boy_height.append(int(number * 0.39) - 66)
  
  result_girl = [[x, y] for x, y in zip(girl_weight, girl_height)]
  data_old = np.array(result_girl)
  all_y_trues_girl = np.ones(ars, dtype=int)


  result_boy = [[x, y] for x, y in zip(boy_weight, boy_height)]
  data_boy = np.array(result_boy)
  all_y_trues_boy = np.zeros(100, dtype=int)
  
  
  data = np.concatenate((data_old, data_boy), axis=0)
  all_y_trues = np.concatenate((all_y_trues_girl, all_y_trues_boy), axis=0)
  
  return data, all_y_trues


if __name__ == "__main__":
  data = generate()[0]
  all_y_trues = generate()[1]
  print(data)
  print('-----------------------------')
  print(all_y_trues)
  import time
  time.sleep(2)
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
  print(data)
  print('-----------------------------')
  print(all_y_trues)