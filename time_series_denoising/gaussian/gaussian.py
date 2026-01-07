import numpy as np
import matplotlib.pyplot as plt

length = 100
k = 15
w = 0.1
noise = np.random.normal(0,1,length)

time = np.linspace(0, 2, length)


final_noise = np.zeros(length)

def gauss(t, w):
    return np.exp((-4*np.log(2)*t*t)/(w*w))

for i in range(length):
    weighted_sum = 0
    weighted_total = 0
    if i-k < 0:
        for j in range(0, i+k):
           g = gauss(time[j]-time[i], w) 
           weighted_sum += g*noise[j]
           weighted_total += g
    elif i+k >= length:
        for j in range(i, length):
            g = gauss(time[j]-time[i],w)
            weighted_sum += g*noise[j]
            weighted_total += g
    else:
        for j in range(i-k, i+k+1):
            g = gauss(time[j]-time[i], w);
            weighted_sum += g*noise[j]
            weighted_total += g
    final_noise[i] = weighted_sum/weighted_total

plt.plot(time, noise, color = "red", label="original noise")
plt.plot(time, final_noise, color="black", label="Smoothed")
plt.xlabel("Time(s)")
plt.ylabel("Y axis")
plt.legend()
plt.grid()
plt.savefig("gaussian_smoothed.png")
plt.show()
