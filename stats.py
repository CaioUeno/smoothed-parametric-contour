import matplotlib.pyplot as plt
import numpy as np
from gaussian_smooth import *
import cv2

def dilation(img, elem_est, origin):
    '''Dilatação de uma imagem binária img utilizando o elemento
       estruturante elem_est. A origem do elemento estruturante
       é indicada pelo ponto origin'''

    num_rows, num_cols = img.shape
    num_rows_ee, num_cols_ee = elem_est.shape
    
    # Armazena as coordenadas do elemento estruturante. As coordenadas
    # são refletidas, de acordo com a definição de dilatação
    set_ee = []
    for row in range(num_rows_ee):
        for col in range(num_cols_ee):
            if elem_est[row, col]==1:
                set_ee.append((origin[0]-row, origin[1]-col))
    
    img_res = np.zeros_like(img)
    for row in range(num_rows):
        for col in range(num_cols):
            z = (row, col)
            has_intersect = intersects(img, set_ee, z)
            if has_intersect:
                img_res[row, col] = 1
                
    return img_res 

def intersects(img, set_ee, z):
    '''Verifica se algum ponto do conjunto set_ee, transladado 
       de uma quantia z, mapeia para um pixel branco na imagem img'''

    for point in set_ee:
        # Translada o ponto
        trans_point = (point[0]+z[0], point[1]+z[1])
        # Verifica ponto somente se ele estiver dentro da imagem
        if trans_point[0]>=0 and trans_point[0]<img.shape[0] and \
           trans_point[1]>=0 and trans_point[1]<img.shape[1]:
        
            if img[trans_point]==1:
                return True
    return False

def stats(img,contour_x, contour_y):

    sigmas = [0.2,2,3,10,20,200]
    perimetros = []
    areas = []
    circ = []
    filter_size = 5
    for sigma in sigmas:
        
        
        smoothed_contour_x = gaussian_smooth_1d(contour_x, filter_size, sigma).astype('int32')
        smoothed_contour_y = gaussian_smooth_1d(contour_y, filter_size, sigma).astype('int32')

        contour_smoothed_values = [[x, y] for x, y in zip(smoothed_contour_x, smoothed_contour_y)]
        img_contour_smoothed = np.zeros(img.shape)
        
        for value in contour_smoothed_values:
            row, col = value
            img_contour_smoothed[row, col] = 1
        
        perimetro = np.sum(np.array(img_contour_smoothed) == 1)
        perimetros.append(perimetro)

        elem_est = np.array([[1, 1],
                     [1, 1]])

        img_res = dilation(img_contour_smoothed, elem_est, origin=(1, 1))
        plt.imshow(img_res)
        plt.show()
        filled_img = img_res.copy()

        for row in range(0,img_res.shape[0]):
            col = 0
            while col < img_res.shape[1]:
                if img_res[row,col] == 1 and img_res[row,col+1] == 0:
                    if any(i == 1 for i in img_res[row,col+1:]):
                        col+=1
                        filled_img[row,col] = 1
                        col+=1
                        while img_res[row,col] == 0:
                            filled_img[row,col] = 1
                            col+=1
                    else:
                        col+=1
                        continue 
                col+=1
    
        area = np.sum(np.array(filled_img) == 1)
        areas.append(area)
        circ.append(4*np.pi*area/(perimetro*perimetro))
        plt.imshow(filled_img)
        plt.show()
        filled_img = np.zeros(img.shape)

    print(perimetros, areas, circ)

    plt.plot(sigmas,areas, label = "Areas")
    plt.plot(sigmas,perimetros, label = "Perímetros")
    plt.plot(sigmas,circ, label = "Circularidades")
    plt.legend(loc="upper left")
    plt.show()
