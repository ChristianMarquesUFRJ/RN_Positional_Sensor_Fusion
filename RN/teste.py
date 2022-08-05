from pandas import read_csv

from tensorflow.keras.layers import GRU, LSTM, SimpleRNN, Input
from tensorflow.keras import Model, Sequential
from tensorflow.keras.callbacks import CSVLogger, ModelCheckpoint
from tensorflow.keras.optimizers import Adam, SGD, Adadelta, RMSprop, Adamax, Adagrad
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.models import model_from_json
from csv_writer import write_data_to_table
from glob import glob
import numpy as np
import pickle
from get_dataSet import get_dataSet

x, y = get_dataSet()

### ========= Load Models ==============

models_names = glob("RN/nNet_models/*.json")
models = []
for model_name in models_names:
    
    with open(model_name, 'r') as json_file:
        architecture = json_file.read()
        model = model_from_json(architecture)
        json_file.close()
    models.append(model)


### ============ Optimizers  ==============

optimizers = [Adam, RMSprop]

### ============ Parameters =================

metrics = None
model:Model = 0

validation_split = 0.2

batch_size = 20

epochs = 20

with open('RN/logs/training_idx.pkl', 'rb') as f:  
    training_idx = pickle.load(f)

### ===================================================

for model_name in models_names:
    
    for optimizer in optimizers:

        with open(model_name, 'r') as json_file:
            architecture = json_file.read()
            model = model_from_json(architecture)
            json_file.close()

        csv_log = CSVLogger(f"RN/logs/csv_log_{training_idx}.csv")
        check = ModelCheckpoint(f"RN/logs/checkpoint_{training_idx}", save_best_only=True)

        model.compile(optimizer=optimizer(), loss="MSE", metrics=metrics)
        model.fit(x = x, y = y, epochs = epochs, validation_split = validation_split, callbacks=[csv_log, check])

        csv_log_dataframe = read_csv(f"RN/logs/csv_log_{training_idx}.csv")
       
        best_result = min(csv_log_dataframe["loss"])
        best_val_result = min(csv_log_dataframe["val_loss"])

        table_data = {
            "training_idx": training_idx,
            "model_name":  model.name,
            "model_params_count": model.count_params(),
            "model_layers_count": model.layers.__len__(),
            "optimizer": optimizer.__name__,
            "optimizer_kwargs": {},
            "loss": "MSE",
            "epochs": epochs,
            "batch_size": batch_size ,
            "validation_split": validation_split,
            "best_result": best_result, 
            "best_val_result": best_val_result
        }

        write_data_to_table(table_path="RN/logs/Data.csv", columns_and_values=table_data, unique_identifier="training_idx")

        training_idx += 1

        with open('RN/logs/training_idx.pkl', 'wb') as f:  
            pickle.dump(training_idx, f)