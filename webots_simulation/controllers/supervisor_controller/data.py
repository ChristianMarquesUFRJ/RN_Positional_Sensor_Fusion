import numpy as np
import os.path

class Data():
    def __init__(self, name_file, size_sample):
        self.size_sample = size_sample
        self.folder_path = "../../../collected_data/"
        self.path = self.folder_path + name_file + ".npy"
        self.first_load = True

        self.arr = np.empty([1,self.size_sample])

        if (os.path.exists(self.path)):
            self.arr = np.load(self.path)
            self.first_load = False
    
    def update(self, sample):
        sample_arr = np.array(sample)
        # print("SAMPLE: ", sample_arr)
        if (self.first_load):
            self.arr[0] = sample_arr
            self.first_load = False
        else:
            self.arr = np.append(self.arr, [sample_arr], axis=0)
        # print("")

    def save(self):
        # print(">> Dados salvos no arquivo: ", self.arr)
        np.save(self.path, self.arr)
