import matplotlib.pyplot as plt
import numpy as np

PATH_GPS_1 = "../../collected_data/gps_real_1.npy"
PATH_GPS_2 = "../../collected_data/gps_real_2.npy"
PATH_POSE = "../../collected_data/pose_real.npy"

DATA_WAY = 150

def get_interval(id):
    first = id*DATA_WAY
    last = first + DATA_WAY

    return (first, last)

def get_compare_data(name_data1, name_data2, interval):
    data1 = np.load(name_data1)
    data2 = np.load(name_data2)

    # print("D1=" + str(len(data1)) + " | D2=" + str(len(data2)))

    d1 = data1[interval[0]:interval[1]]
    d2 = data2[interval[0]:interval[1]]

    return d1, d2

def plot_graph(x1, y1, x2, y2):
    plt.style.use('_mpl-gallery')

    x2, y2 = x2*100000, y2*100000

    # plot
    plt.plot(x1, y1, color='r', linewidth=2)
    plt.plot(x2, y2, color='b', linewidth=2)

    # plt.set(xlim=(0, 5), xticks=np.arange(1, 5),
    #     ylim=(0, 5), yticks=np.arange(1, 5))

    plt.show()

if __name__ == "__main__":
    interval = get_interval(3)
    gps1, pose = get_compare_data(PATH_GPS_1, PATH_POSE, interval)
    plot_graph(pose[:,0], pose[:,1], gps1[:,0], gps1[:,1])
