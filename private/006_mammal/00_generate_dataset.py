#!/usr/bin/env python3
from pathlib import Path

import csv
import numpy as np
import pandas as pd

import os
import librosa

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Watkins Marine Mammal Sounds (https://www.kaggle.com/datasets/shreyj1729/best-of-watkins-marine-mammal-sound-database)
# .wav -> .csv

DATA_PATH = "/home/david/data"

# feature extraction (pulled from tutorial)
header = ['filename', 'length', 'chroma_stft_mean', 'chroma_stft_var', 'rms_mean', 'rms_var', 'spectral_centroid_mean', 'spectral_centroid_var', 'spectral_bandwidth_mean', \
        'spectral_bandwidth_var', 'rolloff_mean', 'rolloff_var', 'zero_crossing_rate_mean', 'zero_crossing_rate_var', 'harmony_mean', 'harmony_var', 'perceptr_mean', \
        'perceptr_var', 'tempo', 'mfcc1_mean', 'mfcc1_var', 'mfcc2_mean', 'mfcc2_var', 'mfcc3_mean', 'mfcc3_var', 'mfcc4_mean', 'mfcc4_var', 'label']

file = open("data.csv", "w", newline = "")
with file:
    writer = csv.writer(file)
    writer.writerow(header)

# 10 classes
marine_mammals = ['AtlanticSpottedDolphin', 'BeardedSeal', 'BlueWhale', 'CommonDolphin', 'DuskyDolphin', 'GraySeal', 'RibbonSeal', 'Long_FinnedPilotWhale', 'RossSeal', 'Rough_ToothedDolphin']

for animal in marine_mammals:
    print(animal)
    for filename in os.listdir(f"{DATA_PATH}/{animal}/"):

        sound_name = f"{DATA_PATH}/{animal}/{filename}"
        y, sr = librosa.load(sound_name, mono = True, duration = 5)
        chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
        rmse = librosa.feature.rms(y = y)
        spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
        spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
        rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y = y, sr = sr)
        to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

        for e in mfcc:
            to_append += f' {np.mean(e)}'

        to_append += f' {animal}'
        file = open('data.csv', 'a', newline = '')

        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())


df = pd.read_csv('data.csv')
print("Dataframe: " + str(df.shape))

class_list = df.iloc[:,-1]
encoder = LabelEncoder()
y = encoder.fit_transform(class_list)

input_parameters = df.iloc[:, 1:27]
scaler = StandardScaler()
X = scaler.fit_transform(np.array(input_parameters))

# training and validation sets
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.2)

dir_private = Path.cwd()
puzzle_name = dir_private.name
dir_public = dir_private.parent.parent / 'public' / puzzle_name
np.savetxt(dir_public / 'train_x_data.csv', train_x, delimiter=',')
np.savetxt(dir_public / 'train_y_data.csv', train_y, delimiter=',')

np.savetxt(dir_public / 'test_x_data.csv', test_x, delimiter=',')
np.savetxt(dir_private / 'test_y_data.csv', test_y , delimiter=',')



## Generate Identity set
header_test = "length chroma_stft_mean chroma_stft_var rms_mean rms_var spectral_centroid_mean spectral_centroid_var spectral_bandwidth_mean \
        spectral_bandwidth_var rolloff_mean rolloff_var zero_crossing_rate_mean zero_crossing_rate_var harmony_mean harmony_var perceptr_mean perceptr_var tempo mfcc1_mean mfcc1_var mfcc2_mean \
        mfcc2_var mfcc3_mean mfcc3_var mfcc4_mean mfcc4_var".split()

file = open('data_test.csv', 'w', newline = '')
with file:
    writer = csv.writer(file)
    writer.writerow(header_test)

# Solution sounds
sounds = ["GraySeal/63001004.wav", "CommonDolphin/5801400X.wav", "RibbonSeal/71013008.wav", "AtlanticSpottedDolphin/6102603L.wav"]

for soundfile in sounds: 
    sound_name = f"{DATA_PATH}/{soundfile}"
    y, sr = librosa.load(sound_name, mono = True, duration = 30)
    chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
    rmse = librosa.feature.rms(y = y)
    spec_cent = librosa.feature.spectral_centroid(y = y, sr = sr)
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    rolloff = librosa.feature.spectral_rolloff(y = y, sr = sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y = y, sr = sr)
    to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'

    for e in mfcc:
        to_append += f' {np.mean(e)}'

    file = open('data_test.csv', 'a', newline = '')

    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())

df_test = pd.read_csv('data_test.csv')
print("Identity Dataframe: " + str(df_test.shape))

identity_test = scaler.transform(np.array(df_test.iloc[:, 0:26]))
np.savetxt(dir_private / 'identity_test.csv', identity_test , delimiter=',')


print('done')
