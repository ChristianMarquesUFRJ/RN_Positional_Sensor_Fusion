import numpy as np


def get_dataSet ():

    pose = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/pose_real.npy")

    gps_real_1 = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/gps_real_1.npy")
    gps_real_2 = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/gps_real_2.npy")

    mpu_1 = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/mpu_1.npy")
    mpu_2 = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/mpu_2.npy")

    encoder = np.load("/home/apeterson056/AutoEncoder/RN_Positional_Sensor_Fusion/collected_data/encoders.npy")

    input_data = np.concatenate((gps_real_1, gps_real_2, mpu_1, mpu_2, encoder), axis=-1)

    input_data = input_data.reshape(int(mpu_1.shape[0]/150), 150, 2*mpu_1.shape[-1] + 2*gps_real_1.shape[-1] + encoder.shape[-1])

    target_data = pose.reshape(int(pose.shape[0]/150), 150, 4)

    return input_data.astype('float32'), target_data.astype('float32')