from PIL import Image
import os
import glob

arr = glob.glob('./11/*.jpg')
toImage = Image.new('RGBA',(1440,900))
i = 0
while(i < 324):
    k = i % 71
    fromImge = Image.open(arr[k])
    fromImge = fromImge.resize((80, 50))  
    # loc = ((i % 2) * 200, (int(i/2) * 200))
    loc = ((int(i/18) * 80), (i % 18) * 50)
    #print(loc)
    toImage.paste(fromImge, loc)
    i+= 1
toImage.save('merged.png')