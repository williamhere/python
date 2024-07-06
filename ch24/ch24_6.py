# ch24_6.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

n_trials = 50
x = np.arange(n_trials)

plt.plot(x, st.binom(n_trials, 0.5).cdf(x), '-o', label='p=0.5, n=50')
plt.plot(x, st.binom(n_trials, 0.6).cdf(x), '-o', label='p=0.6, n=50')
plt.plot(x, st.binom(n_trials, 0.7).cdf(x), '-o', label='p=0.7, n=50')
plt.title("Binomial Distribution")
plt.xlabel("Cumulative Distribution Function")
plt.legend()
plt.show()











