import numpy as nm

def get_data(self, y_axis, label_array, new_array):
  y_axis= nm.concatenate((nm.random.randint(0,10,500), nm.random.randint(0,10,500)))
  label_array= nm.concatenate((nm.full(500,0), nm.full(500,1)))
  new_array= [nm.linspace(0,10,1000), y_axis, label_array]