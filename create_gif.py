# We will create a gif using the imageio package
# first we will import pacakge imageio.v3 v3 for the version 3
import imageio.v3 as iio
#lets give our images in a variable
filenames = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png', 'chicklet4.png']

# now create a empty list
images = []

#lets access the images using for loop
for filename in filenames:
    images.append(iio.imread(filename))

#now we will give the image its duration and loop
iio.imwrite('chicklet.gif', images, duration= 500, loop = 0)