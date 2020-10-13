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
plt.savefig(f"images/{fig_type}.png")

# get contour
contour_x, contour_y = image_contour(img)

filter_size = 5
sigma = 0.5

smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma)
smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma)
