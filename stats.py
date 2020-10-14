import matplotlib.pyplot as plt
import numpy as np
from gaussian_smooth import *
def stats(img,contour_x, contour_y):

    sigmas = [0.2,2,3,10]
    perimetros = []
    areas = []
    circ = []
    filter_size = 5

    for sigma in sigmas:
        
        filled_img = img.copy()
        smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma).astype(int)
        smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma).astype(int)

        contour_smoothed_values = [(x, y) for x, y in zip(smoothed_contour_x, smoothed_contour_y)]
        img_contour_smoothed = np.zeros(img.shape)
        for value in contour_smoothed_values:
            row, col = value
            img_contour_smoothed[row, col] = 1

        perimetro = len(smoothed_contour_x)
        perimetros.append(perimetro)

        for row in range(0,img.shape[1]):
            col = 0
            while col < img.shape[0]:
                if(img[row,col]==1):
                    col += 1
                    while col < img.shape[0] and img[row,col]==0:
                        filled_img[row,col] = 1
                        col += 1
                col += 1
            
        plt.imshow(filled_img)
        plt.show()
    
        area = np.sum(np.array(filled_img) == 1)
        areas.append(area)
        circ.append(4*np.pi*area/(perimetro*perimetro))

    print(perimetros, areas, circ)