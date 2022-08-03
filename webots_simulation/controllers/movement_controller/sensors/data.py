import numpy as np
import os.path

class Data():
    def __init__(self, name_file):
        self.folder_path = "../../../collected_data/"
        self.path = self.folder_path + name_file + ".npy"
        self.first_load = True

        print("Caminho: ", self.path)
        self.arr = np.empty([1,3])

        if (os.path.exists(self.path)):
            print("----------------------")
            self.arr = np.load(self.path)
            # print("LOAD: ", self.arr)
            # self.arr = np.append(self.arr, arr)
            self.first_load = False

        print(self.arr)
    
    def update(self, sample):
        sample_arr = np.array(sample)
        # print("SAMPLE: ", sample_arr)
        # print("ARR: ", self.arr)
        if (self.first_load):
            self.arr[0] = sample_arr
            self.first_load = False
        else:
            self.arr = np.append(self.arr, [sample_arr], axis=0)
        # print("Array: ", self.arr) 
        print("")

    def save(self):
        print("SAVE DATA")
        print("Arquivo: ", self.arr)
        np.save(self.path, self.arr)

    def load(self):
        return np.load(self.path)
