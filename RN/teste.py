import sys, os
import pickle

sys.path.insert(0, os.path.abspath('/home/apeterson056/AutoEncoder/codigoGitHub/IC-AutoEncoder'))
sys.path.insert(0, os.path.abspath('/home/apeterson056/AutoEncoder/codigoGitHub/IC-AutoEncoder/modules'))

from tensorflow.keras.layers import GRU, LSTM, SimpleRNN, Input
from tensorflow.keras import Model, Sequential
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.models import model_from_json
from scikeras.wrappers import KerasRegressor

import numpy as np

from get_dataSet import get_dataSet

x, y = get_dataSet()

x_train = x[:2500]
x_test = x[2500:]

y_train = y[:2500]
y_test = y[2500:]

print("ok")