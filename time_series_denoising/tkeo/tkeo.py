import numpy as np
import matplotlib.pyplot as plt

freq = 300
time = np.linspace(0, 1, freq)

noise = np.random.normal(0, 0.03, freq)
spike_indices = np.random.choice(freq, 5, replace=False)
spikes = np.random.uniform(0.5, 2.0, 5) * np.random.choice([-1, 1], 5)    
noise[spike_indices] = spikes
final_noise = np.zeros(freq)
for i in range(1, freq-1):
    final_noise[i] = noise[i]*noise[i] - noise[i-1]*noise[i+1]
    
final_noise[0] = noise[0]
final_noise[freq-1] = noise[freq-1]

plt.plot(time, noise, color="red", label="EMG Noise")
plt.plot(time, final_noise, color="black", label="Smoothed EMG")
plt.xlabel("Time(s)")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.savefig("EMG_TKEO.png")

plt.show()

