import random
import matplotlib.pyplot as plt
import numpy as np

#If N trials are given then this function finds experimental probability in those N trials
def simulate_aces(num_trials):
    deck = ['Ace'] * 4 + ['Other'] * 48
    success_count = 0
    
    for _ in range(num_trials):
        first_draw = random.choice(deck)
        second_draw = random.choice(deck)
        
        if first_draw == 'Ace' and second_draw == 'Ace':
            success_count += 1
            
    return success_count / num_trials

# 1. Generate N values: 70 points between 100 and 100,000 logarithmically spaced

N_values = np.logspace(np.log10(100), np.log10(100000), num=70, dtype=int)

# 2. Sweep the experimental probability
experimental_probs = []
theoretical_prob = 1 / 169

print("Running 70 simulations. This might take a few seconds...")
for n in N_values:
    prob = simulate_aces(n)
    experimental_probs.append(prob)

# 3. Create the plot
plt.figure(figsize=(10, 6))

# Plot discrete points for the experimental values
plt.scatter(N_values, experimental_probs, color='blue', label='Experimental Probability', zorder=5)

# Plot a continuous horizontal straight line for the theoretical value
plt.axhline(y=theoretical_prob, color='red', linestyle='--', linewidth=2, 
            label=f'Theoretical Probability (1/169 ≈ {theoretical_prob:.5f})', zorder=4)

# Apply Bode plot style formatting (Logarithmic X-axis)
plt.xscale('log')

# Formatting to make it readable and professional
plt.title('Convergence of Probability: Drawing Two Aces (With Replacement)')
plt.xlabel('Number of Trials (N) - Logarithmic Scale')
plt.ylabel('Probability')
plt.grid(True, which="both", linestyle="--", alpha=0.6) # Adds gridlines for both major and minor log ticks
plt.legend()
plt.savefig("../plot.png")

# Display the plot
plt.show()
