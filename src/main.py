# import numpy as np
# def calculate_snr(contaminated_signal, clean_eeg, artifact_segment):
#     # Calculate the signal power (clean EEG)
#     signal_power = np.sum(clean_eeg ** 2)
#     # Calculate the noise power (artifact segment)
#     noise_power = np.sum((contaminated_signal - clean_eeg) ** 2)
#     # Calculate the SNR in dB (RMS FORMULA)
#     snr_db = 10 * np.log10(signal_power / noise_power)
#     return snr_db
#
# # Example usage:
# clean_eeg = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# artifact_segment = np.array([0.1, 0.2, 0.3, 0.2, 0.1])
# λ = 0.5
#
# contaminated_signal = clean_eeg + λ * artifact_segment
# snr = calculate_snr(contaminated_signal, clean_eeg, artifact_segment)
# print("SNR:", snr)

# import random
# import numpy as np
# import inspect
# random_decimal = round(random.uniform(0,1.7),1)
# print(np.random.uniform(0,1.7,2))
# print(random_decimal)

import numpy as np
from PyEMD import EMD
import matplotlib.pyplot as plt

T = np.linspace(0, 1, 100)
S = np.sin(2*2*np.pi*T)
emd = EMD(extrema_detection='parabol')
IMFs = emd.emd(S)
IMFs.shape
print(IMFs.shape)
plt.plot(T,S)
plt.plot(IMFs)
plt.show()


#DUMMY

# def calculate_snr(clean_eeg, artifact_segment,λ):
#     N = 512
#     # Calculate the signal power (clean EEG)
#     signal_power = (np.sum(clean_eeg ** 2)*(1/N))**0.5
#     # Calculate the noise power (artifact segment)
#     noise_power = (np.sum((λ*artifact_segment)**2)*(1/N))**0.5
#     # Calculate the SNR in dB (RMS FORMULA)
#     snr_db = 10 * np.log10(signal_power / noise_power)
#     return round(snr_db,2)


# def generate_contaminated_signal(clean_eeg_data,artifact_data,num_samples:int, artifact_type:str):
#     num_clean_eeg_samples = clean_eeg_data.shape[0]
#     num_eog_artifacts = artifact_data.shape[0]
#
#     contaminated_eeg_data = []
#     contamination_indices = []
#     snr_values=[]
#
#     for i in range(num_samples):
#         clean_eeg_index = np.random.randint(0, num_clean_eeg_samples)
#         eog_artifact_index = np.random.randint(0, num_eog_artifacts)
#
#         clean_eeg_sample = clean_eeg_data[clean_eeg_index]
#         artifact = artifact_data[eog_artifact_index]
#
#         #TYPICAL SNR RANGE ACCORDING TO PREVIOUS STUDIES
#         if artifact_type =='ocular':
#             snr_range = [-7,2]
#         elif artifact_type == 'myogenic':
#             snr_range = [-7,4]
#
#         #GENERATE RANDOM LAMBDA VALUE HERE
#         accepted = False
#         while accepted == False:
#             λ = random.uniform(-40,40)
#             #Generate contaminated signal using formula: y=x+(λ*n)
#             contaminated_eeg_sample = clean_eeg_sample + (artifact*λ)
#             #Calculate SNR
#             snr=calculate_snr(clean_eeg_data,artifact,λ)
#             if snr>=snr_range[0] and snr<=snr_range[1]:
#                 accepted=True
#
#         #ADD CONTAMINATED SIGNAL TO FINAL ARRAY OF DATA TO BE USED FOR TESTING
#         contaminated_eeg_data.append(contaminated_eeg_sample)
#         contamination_indices.append((clean_eeg_index, eog_artifact_index))
#         snr_values.append(snr)
#     return np.array(contaminated_eeg_data), contamination_indices, snr_values, artifact_type