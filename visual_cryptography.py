from PIL import Image
import numpy as np

image1 = Image.open('scrambled1.png')
image2 = Image.open('scrambled2.png')

# Turn into arrays, act like matrices.
array1 = np.array(image1)
array2 = np.array(image2)

# Matrix addition
array = np.add(array1, array2)

# Make image from new array
stacked_image = Image.fromarray(array)

stacked_image.save('secret.png')  # Save the image to a file