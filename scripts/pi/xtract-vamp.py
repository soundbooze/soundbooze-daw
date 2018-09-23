import vamp
import librosa
import numpy as np

filename = 'audio.wav'

data, sr = librosa.load(filename)

bark_coefficients_matrix = vamp.collect(data, sr, "vamp-libxtract:bark_coefficients")
mfcc_matrix = vamp.collect(data, sr, "vamp-libxtract:mfcc")
spectral_skewness_vector = vamp.collect(data, sr, "vamp-libxtract:spectral_skewness")
spectral_centroid_vector = vamp.collect(data, sr, "vamp-libxtract:spectral_centroid")
spectral_kurtosis_vector = vamp.collect(data, sr, "vamp-libxtract:spectral_kurtosis")
spectral_slope_vector = vamp.collect(data, sr, "vamp-libxtract:spectral_slope")

mfcc = mfcc_matrix['matrix'][1]
bark = bark_coefficients_matrix['matrix'][1]
spectral_skewness = spectral_skewness_vector['vector'][1]
spectral_centroid = spectral_centroid_vector['vector'][1]
spectral_kurtosis = spectral_kurtosis_vector['vector'][1]
spectral_slope = spectral_slope_vector['vector'][1]

#print mfcc
#print bark
#print spectral_slope

