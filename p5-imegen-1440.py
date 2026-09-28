import cv2 
# leer la imagen con cv2
img = cv2.imread('Perro.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrando imagen en ventana de titulo
cv2.imshow('El perro 1440', img)
# el tiempo de espera
cv2.waitKey(0)
#destruir todas las ventanas
cv2.destroyAllWindows()
