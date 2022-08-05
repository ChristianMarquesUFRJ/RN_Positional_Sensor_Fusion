import numpy as np
from pandas import DataFrame
import pickle
training_idx = 0

with open('RN/logs/training_idx.pkl', 'wb') as f:  
    pickle.dump(training_idx, f)