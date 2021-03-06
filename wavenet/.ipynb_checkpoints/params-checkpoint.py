import os

"""Parameters related to Data"""
sampling_rate = 8192
mu = 256 # mu of waveform in 8 bits when the data is mu-law encoded
accel_chans =  [11, 12, 13, 29, 30, 31, 47, 48, 49, 62, 63, 64]
rescale_factor = 100

"""Paths"""
PATH = "/data/datasets/hyundai"
ACC_DATA = os.path.join(PATH, "stationary_accel_data.pickle")
SOUND_DATA = os.path.join(PATH, "stationary_sound_data.pickle")

ACC_NPY = os.path.join(PATH, "acc_win_512_hop_128.npy")
SOUND_NPY = os.path.join(PATH, "sound_win_512_hop_128.npy")
