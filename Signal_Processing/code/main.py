import numpy as np
import matplotlib.pyplot as plt

# Initialize the frequency axis. 
# The range [-3, 3] kHz is selected to provide a clear view of the baseband and adjacent spectral replicas.
f = np.linspace(-3, 3, 1000)

@np.vectorize  
def original_spectrum(freq):
    if freq < -1 or freq > 1:
        return 0.0
    elif freq >= 0:
        return 1.0 - freq
    else: 
        return 1.0 + freq
        
# Define the sampling frequency (fs) in kHz.
fs = 1.0

# Initialize an array to store the accumulated sum of all spectral replicas.
sampled_spectrum = np.zeros_like(f)

# Initialize a list to store individual shifted spectra for visualization purposes.
replicas = []

# Simulate the infinite summation of the sampled spectrum.
# A finite range (n = -5 to 5) is utilized as an approximation for computational feasibility.
n_values = range(-5, 6)
for n in n_values:
    # Calculate the frequency shift for the nth harmonic: M(f - n*fs).
    shifted_triangle = original_spectrum(f - n * fs)
    replicas.append(shifted_triangle)
    
    # Superimpose the shifted spectrum onto the total sampled spectrum array.
    sampled_spectrum += shifted_triangle

# --- Visualization and Plotting Formatting ---

plt.figure(figsize=(10, 6))

# Plot the individual shifted spectral replicas.
for i, replica in enumerate(replicas):
    if i == 5: # Highlights the n=0 baseband spectrum in the legend.
        plt.plot(f, replica, '--', color='blue', alpha=0.6, label='Individual Shifted Spectra')
    else:
        plt.plot(f, replica, '--', color='blue', alpha=0.6)

# Plot the final superimposed spectrum to illustrate aliasing effects.
plt.plot(f, sampled_spectrum, '-', color='red', linewidth=3, label='Final Sampled Spectrum (Sum)')

# Apply academic formatting to the plot axes, grid, and legend.
plt.title('Frequency Spectrum of Ideally Sampled Signal ($f_s = 1$ kHz)')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude')
plt.xlim(-3, 3)
plt.ylim(0, 1.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Export the figure and render the plot display.
plt.tight_layout()
plt.savefig("../plot.png")
plt.show()
