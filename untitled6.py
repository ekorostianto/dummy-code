import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn


# Fixing random state for reproducibility
np.random.seed(19680801)
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), 1, 11)

cax = ax.imshow(data, cmap=cm.coolwarm_r)
ax.set_title('Gaussian noise with vertical colorbar')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
cbar.ax.set_yticklabels(['exceptional drought', 'extreme drought', 'severe drought', 'moderate drought', 'abnormally dry', 'near normal', 'slightly wet', 'moderately wet', 'very wet', 'extremely wet', 'exceptionally wet'])  # vertically oriented colorbar