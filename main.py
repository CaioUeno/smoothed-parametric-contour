import numpy as np
import matplotlib.pyplot as plt
from objects import *
from gaussian_smooth import *
from moore_neighbor_tracing import image_contour

fig_type = input("Select a figure: Cross, Square, Triangle, Circle or Random: ").lower()
if fig_type == "cross":
    img = cross()
elif fig_type == "square":
    img = square()
elif fig_type == "triangle":
    img = triangle()
elif fig_type == "circle":
    img = circle()
elif fig_type == "random":
    img = random()
else:
    raise Exception("Wrong Input Type")

plt.imshow(img)
plt.savefig(f"images/base/{fig_type}.png")


# Get object contour
contour_x, contour_y = image_contour(img)
contour_values = [(x, y) for x, y in zip(contour_x, contour_y)]
img_contour = np.zeros(img.shape)
for value in contour_values:
    row, col = value
    img_contour[row, col] = 1

plt.imshow(img_contour)
plt.savefig(f"images/contour/{fig_type}_contour.png")

# Apply gaussian smoothing
filter_size = 5
sigma = 0.5

smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma)
smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma)

# contour_smoothed_values = [(x, y) for x, y in zip(smoothed_contour_x, smoothed_contour_y)]
# img_contour_smoothed = np.zeros(img.shape)
# for value in contour_smoothed_values:
#     row, col = value
#     img_contour_smoothed[row, col] = 1

plt.imshow(img_contour_smoothed)
plt.savefig(f"images/smoothed/{fig_type}_smoothed.png")

