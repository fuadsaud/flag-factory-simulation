import numpy as np
from scipy import stats
import matplotlib.pyplot as plot

np.random.seed(0)
randoms = np.random.random_integers(1, 100, 1000)

freqs = stats.itemfreq(randoms)
freqs = freqs[freqs[:,1].argsort()]

x = np.array([r[0] for r in freqs])
y = np.array([r[1] for r in freqs])

# plot.figure(1)

# plot.subplot(221)
plot.bar(x, y)
# plot.axvline(randoms.mean(), color='red')
plot.grid(True)

# plot.subplot(222)
# plot.bar(x, y)
# plot.axvline(randoms.mean(), color='red')
# plot.grid(True)

plot.show()
