## EMD CODE DRAFTS
```.py
signal = eeg_samples[0]
imfs,residual = emd(signal)
```

### Draft 1
```.py
# import numpy as np
# from scipy.interpolate import CubicSpline

# def find_extrema(signal):
#     # Find local minima and maxima
#     minima = (np.diff(np.sign(np.diff(signal))) > 0).nonzero()[0] + 1
#     maxima = (np.diff(np.sign(np.diff(signal))) < 0).nonzero()[0] + 1
#     return minima, maxima

# def get_envelope(signal, extrema):
#     envelope = CubicSpline(extrema, signal[extrema], bc_type='natural')
#     return envelope(np.arange(len(signal)))

# def is_imf(signal):
#     minima, maxima = find_extrema(signal)
#     num_zero_crossings = len(np.where(np.diff(np.sign(signal)) != 0)[0])
#     print(f"Min: {len(minima)}, Max: {len(maxima)}, ZCs: {num_zero_crossings}")
#     return abs(len(minima) - len(maxima)) <= 1 and num_zero_crossings <= 1

# def emd(signal):
#     imfs = []
#     residual = signal.copy()
#     potential = 0

#     while True:
#         prev_residual = residual.copy()

#         # Step 1: Identify extrema of the signal
#         minima, maxima = find_extrema(residual)

#         # Step 2: Use cubic spline interpolation to get upper and lower envelopes
#         lower_envelope = get_envelope(residual, minima)
#         upper_envelope = get_envelope(residual, maxima)

#         # Step 3: Calculate mean of the envelopes
#         mean_envelope = 0.5 * (lower_envelope + upper_envelope)

#         # Step 4: Subtract mean envelope from the signal to get a potential IMF
#         potential_imf = residual - mean_envelope
#         potential+=1
#         print(f"Potential IMF # {potential}")

#         # Step 5: Check if potential_imf is an IMF
#         if is_imf(potential_imf):
#             print("IMF discovered")
#             # Step 6: Check if it differs from the previous IMF
#             if len(imfs) > 0 and np.sum((imfs[-1] - potential_imf) ** 2) < 1e-10:
#                 break  # Stop if no significant change from the previous IMF
#             imfs.append(potential_imf)
#         else:
#             # Step 7: Assign potential_imf as the new residual and iterate
#             residual = potential_imf

#         # Step 8: Stopping criterion - Zero Crossings Criterion
#         zero_crossings = len(np.where(np.diff(np.sign(potential_imf)) != 0)[0])
#         if zero_crossings < 2:
#             break  # Stop if number of zero-crossings decreases

#     return imfs, residual
```


### Draft 2
```.py
# # def find_extrema(signal):
# #     # Find local minima and maxima
# #     minima = (np.diff(np.sign(np.diff(signal))) > 0).nonzero()[0] + 1
# #     maxima = (np.diff(np.sign(np.diff(signal))) < 0).nonzero()[0] + 1
# #     return minima, maxima

# def find_extrema(signal):
#     maxima = [(i, signal[i]) for i in range(1, len(signal) - 1) if signal[i - 1] < signal[i] > signal[i + 1]]
#     minima = [(i, signal[i]) for i in range(1, len(signal) - 1) if signal[i - 1] > signal[i] < signal[i + 1]]
#     return maxima, minima


# def extract_mean_envelope(maxima, minima, signal_length=512):
#     upper_envelope = np.interp(np.arange(signal_length), *zip(*maxima))
#     lower_envelope = np.interp(np.arange(signal_length), *zip(*minima))
#     mean_envelope = (upper_envelope + lower_envelope) / 2
#     return upper_envelope, lower_envelope, mean_envelope

# def is_imf(signal):
#     minima, maxima = find_extrema(signal)
#     num_zero_crossings = len(np.where(np.diff(np.sign(signal)) != 0)[0])
#     print(f"Min: {len(minima)}, Max: {len(maxima)}, ZCs: {num_zero_crossings}")
#     return abs(num_zero_crossings - len(minima)) <=1 or abs(num_zero_crossings - len(maxima)) <=1

# def emd(signal):
#     imfs = []
#     residual = signal
#     potential = 0
#     imf_count = 0

#     while True:
#         # Step 1: Identify extrema of the signal
#         minima, maxima = find_extrema(residual)

#         # Step 2: Use cubic spline interpolation to get upper and lower envelopes
#         # Step 3: Calculate mean of the envelopes
#         upper, lower, mean = extract_mean_envelope(minima,maxima)

#         # Step 4: Subtract mean envelope from the signal to get a potential IMF
#         potential_imf = residual - mean
#         potential+=1
#         print(f"Potential IMF # {potential}")

#         # Step 5: Check if potential_imf is an IMF
#         if is_imf(potential_imf):
#             imf_count +=1
#             print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMF discovered # {imf_count}")
#             # Step 6: Check if it differs from the previous IMF
#             if len(imfs) > 0 and np.sum((imfs[-1] - potential_imf) ** 2) < 1e-10:
#                 break  # xStop if no significant change from the previous IMF
#             imfs.append(potential_imf)
#         else:
#             # Step 7: Assign potential_imf as the new residual and iterate
#             residual = potential_imf

#         # Step 8: Stopping criterion - Zero Crossings Criterion
#         zero_crossings = len(np.where(np.diff(np.sign(potential_imf)) != 0)[0])
#         if zero_crossings < 2:
#             break  # Stop if number of zero-crossings decreases

#     return imfs, residual

```


### Draft 3
```.py
def find_extrema(signal):
    diff_signal = np.diff(signal)
    maxima = (diff_signal[:-1] > 0) & (diff_signal[1:] < 0)
    minima = (diff_signal[:-1] < 0) & (diff_signal[1:] > 0)
    maxima_indices = np.where(maxima)[0] + 1
    minima_indices = np.where(minima)[0] + 1
    maxima_values = signal[maxima_indices]
    minima_values = signal[minima_indices]
    return list(zip(maxima_indices, maxima_values)), list(zip(minima_indices, minima_values))

def extract_mean_envelope(maxima, minima, signal_length=512):
    upper_envelope = np.interp(np.arange(signal_length), *zip(*maxima))
    lower_envelope = np.interp(np.arange(signal_length), *zip(*minima))
    mean_envelope = (upper_envelope + lower_envelope) / 2
    return upper_envelope, lower_envelope, mean_envelope

def is_imf(signal):
    minima, maxima = find_extrema(signal)
    num_zero_crossings = len(np.where(np.diff(np.sign(signal)) != 0)[0])
    return abs(num_zero_crossings - len(minima)) <= 1 or abs(num_zero_crossings - len(maxima)) <= 1

def emd(signal):
    imfs = []
    residual = signal
    potential = 0
    imf_count = 0

    while True:
        # Step 1: Identify extrema of the signal
        maxima, minima = find_extrema(residual)

        # Step 2 & 3: Interpolate upper and lower envelopes, calculate mean
        upper, lower, mean = extract_mean_envelope(maxima, minima)

        # Step 4: Subtract mean envelope from the signal to get a potential IMF
        potential_imf = residual - mean
        potential += 1
        print(f"Potential IMF # {potential}")

        # Step 5: Check if potential_imf is an IMF
        if is_imf(potential_imf):
            imf_count += 1
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMF discovered # {imf_count}")
            # Step 6: Check if it differs from the previous IMF
            if len(imfs) > 0 and np.allclose(imfs[-1], potential_imf, atol=1e-10):
                break  # Stop if no significant change from the previous IMF
            imfs.append(potential_imf)
        else:
            # Step 7: Assign potential_imf as the new residual and iterate
            residual = potential_imf

        # Step 8: Stopping criterion - Zero Crossings Criterion
        zero_crossings = len(np.where(np.diff(np.sign(potential_imf)) != 0)[0])
        if zero_crossings < 2:
            break  # Stop if number of zero-crossings decreases

    return imfs, residual
```

