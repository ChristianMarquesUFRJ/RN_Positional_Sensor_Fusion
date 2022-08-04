import matplotlib.pyplot as plt
import numpy as np

PATH_POSE = "../../collected_data/pose_real.npy"
PATH_GPS_1 = "../../collected_data/gps_real_1.npy"
PATH_GPS_2 = "../../collected_data/gps_real_2.npy"
PATH_ENCODER = "../../collected_data/encoders.npy"

SAMPLE_ID = 4

DATA_WAY = 150
DT_INTERVAL = 0.2

def get_interval(id):
    first = id*DATA_WAY     # Ex.: 0,   150, 300
    last = first+DATA_WAY-1 # Ex.: 149, 299, 449
    return (first, last)

def get_compare_data(name_data, interval):
    data = np.load(name_data)
    return data[interval[0]:interval[1]]

def format_gps(lat, long):
    return lat*100000, long*100000

def format_encoders(linear_speed, angular_speed):
    size = len(linear_speed)
    x, y, a = [0.0]*size, [0.0]*size, [0.0]*size

    for i in range(size):
        x_, y_, a_ = 3.94324, 2.86244, 0.649943
        if (i > 0):
            x_, y_, a_ = x[i-1], y[i-1], a[i-1]

        a[i] = a_ + angular_speed[i]*DT_INTERVAL
        x[i] = x_ + (DT_INTERVAL*linear_speed[i])*(np.cos(a[i]))
        y[i] = y_ + (DT_INTERVAL*linear_speed[i])*(np.sin(a[i]))
        
    return x, y, a


def plot_graph(pose_xy, gps_xy, encoders_xy):
    plt.style.use('_mpl-gallery')

    gps_xy = format_gps(gps_xy[0], gps_xy[1])
    encoders_xy = format_encoders(encoders_xy[0], encoders_xy[1])

    # plot
    fig, ax = plt.subplots()
    ax.plot(pose_xy[:][0], pose_xy[:][1], label='Referência', color='r', linewidth=2)
    ax.plot(gps_xy[:][0], gps_xy[:][1], label='GPS', color='b', marker='o', linestyle=':', linewidth=0.5)
    ax.plot(encoders_xy[:][0], encoders_xy[:][1], label='Encoder', color='g', linewidth=2)
    
    legend = ax.legend(loc='lower left', shadow=True, fontsize='medium')

    plt.show()

if __name__ == "__main__":
    interval = get_interval(SAMPLE_ID)

    pose = get_compare_data(PATH_POSE, interval)
    gps1 = get_compare_data(PATH_GPS_1, interval)
    encoders = get_compare_data(PATH_ENCODER, interval)

    pose_xy = (pose[:,0], pose[:,1])
    gps_xy = (gps1[:,1], gps1[:,0])
    encoders_xy = (encoders[:,0], encoders[:,1])
    plot_graph(pose_xy, gps_xy, encoders_xy)
