import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
W = 1000.0          # Bandwidth in Hz
Ts = 0.001          # Sampling interval (1 ms)
t_max = 0.005       # Plot from -5 ms to +5 ms

# --- 1. Continuous Time Signal ---
t_cont = np.linspace(-t_max, t_max, 1000)
u_cont = W * (np.sinc(W * t_cont))**2

# --- 2. Sampled Time Signal ---
t_disc = np.arange(-t_max, t_max + Ts, Ts)
u_disc = W * (np.sinc(W * t_disc))**2

# --- 3. Fourier Transform of the Sampled Signal ---
N = len(u_disc)

# Calculate the FFT of the discrete samples
# We use ifftshift to correctly align the t=0 point for the algorithm
U_sampled_complex = np.fft.fft(np.fft.ifftshift(u_disc))

# Get the magnitude of the frequency spectrum and center 0 Hz
U_sampled_mag = np.abs(np.fft.fftshift(U_sampled_complex))

# Generate the corresponding frequency axis
freq_axis = np.fft.fftshift(np.fft.fftfreq(N, Ts))

# --- Plotting ---
plt.figure(figsize=(16, 5)) # Made the figure wider to fit 3 plots

# Subplot 1: Continuous Time Signal
plt.subplot(1, 3, 1)
plt.plot(t_cont * 1000, u_cont, color='blue', linewidth=2)
plt.title('1. Continuous Signal: $u(t)$')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(-5, 5)

# Subplot 2: Sampled Time Signal
plt.subplot(1, 3, 2)
plt.plot(t_cont * 1000, u_cont, color='blue', linewidth=1, alpha=0.2)
markerline, stemlines, baseline = plt.stem(t_disc * 1000, u_disc, basefmt="k-")
plt.setp(markerline, color='red', markersize=8)
plt.setp(stemlines, color='red', linewidth=2)
plt.title('2. Sampled Signal: $u(nT_s)$')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(-5, 5)

# Subplot 3: Frequency Spectrum of Sampled Signal
plt.subplot(1, 3, 3)
# Plotting the discrete frequency bins connected by a line to show the shape
plt.plot(freq_axis, U_sampled_mag, color='red', linewidth=3, marker='o')
plt.title('3. Spectrum of Sampled Signal: $|U_s(f)|$')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True, linestyle='--', alpha=0.7)
# Setting Y-axis to clearly show it's a constant, non-zero flat line
plt.ylim(0, max(U_sampled_mag) * 1.5) 

plt.tight_layout()
plt.savefig("../plot2.png")
plt.show()
