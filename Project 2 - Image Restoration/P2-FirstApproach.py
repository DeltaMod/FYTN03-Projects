from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

original = imread('EM_ScreamGS.bmp')[:,:,0]
mask = imread('mask.bmp')[:,:,0]

plt.figure()
plt.imshow(original, cmap='gray')
plt.title('Original Image')
plt.show()

plt.figure()
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.show()