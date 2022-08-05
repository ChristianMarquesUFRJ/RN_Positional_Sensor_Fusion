from tensorflow.keras.layers import GRU, LSTM, SimpleRNN, Input
from tensorflow.keras import Model, Sequential
from tensorflow.keras.utils import plot_model

model_name = "SimpleRNN_sequencial_4.0"

input_layer = Input(shape=(None, 26))
output_layer = SimpleRNN(units = 100, return_sequences = True, activation='relu')(input_layer)
output_layer1 = SimpleRNN(units = 200, return_sequences = True, activation='relu')(output_layer)
output_layer2 = SimpleRNN(units = 500, return_sequences = True, activation='relu')(output_layer1)
output_layer3 = SimpleRNN(units = 300, return_sequences = True, activation='relu')(output_layer2)
output_layer4 = SimpleRNN(units = 100, return_sequences = True, activation='relu')(output_layer3)
output_layer5 = SimpleRNN(units = 4, return_sequences = True, activation=None)(output_layer4)

model = Model(inputs=input_layer, outputs=output_layer5, name = model_name)

model_json = model.to_json(indent = 4)

with open("RN/nNet_models/" + model_name + ".json", "w") as json_file:
    json_file.write(model_json)
    json_file.close()

plot_model(model=model, to_file="RN/nNet_models/PNG-Models/" + model_name + '.png', show_shapes=True, rankdir= "TB", expand_nested=True )

model.summary()