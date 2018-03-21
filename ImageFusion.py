from PIL import Image
import glob
import numpy as np

# path to the images
arr = glob.glob('./11/*.jpg')
toImage = Image.new('RGBA',(1440,900))
i = 0
# the whole images are 1440 * 900  
# each image is 80 * 50 

# image splice
while(i < 324):
    k = i % len(arr)
    fromImge = Image.open(arr[k])
    fromImge = fromImge.resize((80, 50))  
    # loc = ((i % 2) * 200, (int(i/2) * 200))
    loc = ((int(i/18) * 80), (i % 18) * 50)
    #print(loc)
    toImage.paste(fromImge, loc)
    i+= 1

im2 = toImage
# path to target image
im1 = Image.open('.\IMG_019.jpg')
im1 = im1.resize((1440,900))
toImage2 = Image.new('RGBA',(1440,900))
toImage2.paste(im1, (0,0))
#toImage.show(toImage)
# fusion parameter
alpha = 0.35
im1 = toImage2

im1 = np.array(im1)
im2 = np.array(im2)
# fusion
newim = im1*(1-alpha) + im2*alpha
newim=Image.fromarray(np.uint8(newim)) 
#save image
newim.save("fusionIm.png")




