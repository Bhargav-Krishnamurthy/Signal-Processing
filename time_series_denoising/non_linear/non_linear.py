import numpy as np
import matplotlib.pyplot as plt

N = 500
t = np.linspace(0, 10, N)

signal = np.sin(2 * np.pi * 1.2 * t)

true_trend = 0.05*t**2 - 0.3*t + 2

# Observed signal
x = signal+ true_trend 


t_norm = (t - np.mean(t)) / np.std(t)

# Polynomial degree (2 = quadratic trend)
degree = 2

# Fit polynomial
coeffs = np.polyfit(t_norm, x, degree)

# Evaluate fitted polynomial (estimated trend)
estimated_trend = np.polyval(coeffs, t_norm)


x_detrended = x - estimated_trend

# Plotting

plt.figure(figsize=(12, 8))

# Original signal
plt.subplot(3, 1, 1)
plt.plot(t, x, label="Observed Signal", alpha=0.7)
plt.plot(t, true_trend, 'k--', label="True Trend")
plt.title("Observed Signal with Non-Linear Trend")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Estimated trend
plt.subplot(3, 1, 2)
plt.plot(t, x, label="Observed Signal", alpha=0.4)
plt.plot(t, estimated_trend, 'r', linewidth=2, label="Estimated Polynomial Trend")
plt.title("Polynomial Trend Estimation (Least Squares)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Detrended signal
plt.subplot(3, 1, 3)
plt.plot(t, x_detrended, 'g', label="Detrended Signal")
plt.title("Signal After Non-Linear Detrending")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.savefig("Non_linear.png")
plt.show()



print("Estimated polynomial coefficients (highest degree first):")
print(coeffs)

