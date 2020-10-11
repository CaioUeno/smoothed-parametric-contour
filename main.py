import numpy as np
import matplotlib.pyplot as plt
from objects import *
from gaussian_smooth import *

img = cross() # can change later

# get contour

contour_x = # to complete
contour_y = # to complete

filter_size = 5
sigma = 0.5

smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma)
smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma)
