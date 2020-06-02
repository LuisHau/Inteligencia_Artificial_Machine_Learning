import cv2
import numpy as np

image = cv2.imread('pyimg.jpg')

#Tamaño de la Imagen
imageOut = cv2.resize(image,(400,200),interpolation=cv2.INTER_CUBIC)

#Para recorte de la imagen
#print('image.shape=',image.shape)
#imageOut = image[100:300,150:600]
#ancho = image.shape[1] #columnas
#alto = image.shape[0] # filas

# Rotacion
#M = cv2.getRotationMatrix2D((ancho/2,alto/2),90,.5)
#imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()
