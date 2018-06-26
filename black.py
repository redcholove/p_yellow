from skimage import io
import matplotlib.pyplot as plt 
import numpy as np

def reduceThree(image): 
    rows,cols,dims=image.shape
    ret_img = np.uint8(np.zeros((rows,cols,3))) 
    for i in range(0,rows):
        for j in range(0,cols): 
            luminance = 0 #int 
            for k in range(0,3):
                luminance = luminance + image[i,j,k] 
            luminance = luminance/3 #float!?
            if luminance < 64:
                ret_img[i,j,0] = 0
                ret_img[i,j,1] = 0
                ret_img[i,j,2] = 0
            elif luminance > 120: 
                ret_img[i,j,0] = 255 
                ret_img[i,j,1] = 255 
                ret_img[i,j,2] = 255
            else:
                ret_img[i,j,0] = 255 
                ret_img[i,j,1] = 255 
                ret_img[i,j,2] = 0
                
    return ret_img 

img=io.imread('black_man.jpg')
io.imshow(img)

img2 = reduceThree(img)
plt.figure()
io.imshow(img2)
io.show()