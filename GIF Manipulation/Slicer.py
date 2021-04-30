from PIL import Image
from PIL import ImageFile
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True
#numKeyFrames = 20

#sliceGIF takes a GIF file and slices it into individual frames
def sliceGIF(file):
    with Image.open(file) as image:
        for i in range(image.n_frames):
            image.seek(i)
            image.save(f'./frames/{i}.bmp')
            print(f'Saved frame{i} as {i}.bmp')
        image.close()


# constructGIF pulls all files from a directory and attempts to stitch them into a GIF 
def constructGIF(directory, savename):
    images = []
    for filename in os.listdir(directory):
        images.append(Image.open(directory+'\\'+filename))
        print(f'added {filename} to frame list')
    images[0].save(f'{savename}.gif',
                       format='GIF',
                       save_all = True,
                       append_images = images[1:],
                       optimize = True,
                       loop = 0
                   )
    for image in images:

        image.close()

# createInterpolate takes files froma directory and creates additional images that are interpolated between 2 existing images
def createInterpolate(directory):
    images = []
    for filename in os.listdir(directory):
        images.append(Image.open(directory+'\\'+filename))
        print(f'added {filename} to images list')
    imcount = 0
    print("image list: ",images)
    for i in images:
        print(f"blending {imcount} and {imcount+1}")
        print(i)
        im = Image.blend(images[imcount],images[imcount+1],0.5)
        print(im)
        print("saving blended image")
        im.save(directory+'\\'+ str((imcount+0.75))+'.jpg')
        imcount += 1

createInterpolate('.\\bmpdream')

        
