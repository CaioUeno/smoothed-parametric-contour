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
        img_contour_smoothed = 0
        smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma).astype(int)
        smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma).astype(int)

        contour_smoothed_values = [(x, y) for x, y in zip(smoothed_contour_x, smoothed_contour_y)]
        img_contour_smoothed = np.zeros(img.shape)
        
        for value in contour_smoothed_values:
            row, col = value
            img_contour_smoothed[row, col] = 1

        plt.plot(smoothed_contour_y,smoothed_contour_x)
        plt.show()
        plt.imshow(img_contour_smoothed)
        plt.show()
        
        perimetro = len(smoothed_contour_x)
        perimetros.append(perimetro)
        for row in range(0,img.shape[0]):
            col = 0
            # if (np.sum(np.array(filled_img[row]) == 1)%2) != 0:
            #     print(filled_img[row])
            #     continue
            while col < filled_img.shape[1]:
                if(col < filled_img.shape[1]) and (filled_img[row,col]==1):
                    print('começar a pintar '+str(row)+','+str(col) )
                    col += 1
                    while col < filled_img.shape[1] and filled_img[row,col]==0:
                        print(row,col)
                        filled_img[row,col] = 1
                        col += 1
                col += 1
            
    
        area = np.sum(np.array(filled_img) == 1)
        areas.append(area)
        circ.append(4*np.pi*area/(perimetro*perimetro))

    print(perimetros, areas, circ)