import numpy as np
import matplotlib.pyplot as plt

# 1. Define the frequency axis (from -3 kHz to 3 kHz for a good view)
f = np.linspace(-3, 3, 1000)

# 2. Define the original spectrum function (a triangle from -1 to 1)
def original_spectrum(freq):
    # Returns a triangle: max height 1 at center, hitting 0 at +/- 1
    return np.maximum(1 - np.abs(freq), 0)

# 3. Define the sampling frequency based on the problem
fs = 1.0  # 1 kHz

# 4. Create the shifted replicas
# We will sum a few replicas (from n=-5 to n=5) to simulate the infinite sum
sampled_spectrum = np.zeros_like(f)
replicas = []

n_values = range(-5, 6)
for n in n_values:
    # Shift the original spectrum by n * fs
    shifted_triangle = original_spectrum(f - n * fs)
    replicas.append(shifted_triangle)
    sampled_spectrum += shifted_triangle

# 5. Plotting the results
plt.figure(figsize=(10, 6))

# Plot the individual shifted triangles (dashed lines)
for i, replica in enumerate(replicas):
    if i == 5: # n=0, the original baseband
        plt.plot(f, replica, '--', color='blue', alpha=0.6, label='Individual Shifted Spectra')
    else:
        plt.plot(f, replica, '--', color='blue', alpha=0.6)

# Plot the final summed spectrum (solid thick line)
plt.plot(f, sampled_spectrum, '-', color='red', linewidth=3, label='Final Sampled Spectrum (Sum)')

# Formatting the plot
plt.title('Frequency Spectrum of Ideally Sampled Signal ($f_s = 1$ kHz)')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude')
plt.xlim(-3, 3)
plt.ylim(0, 1.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("../plot.png")
plt.show()
