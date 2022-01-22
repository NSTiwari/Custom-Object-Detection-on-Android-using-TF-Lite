import PIL.Image
import glob
import os

images = [i for i in glob.glob("./dataset/*.jpg")]

jpeg = 0
others = 0

for i in images:
	img = PIL.Image.open(i)
	if img.format == 'JPEG':
		jpeg += 1
	else:
		print('{} is {}'.format(i, img.format))
		others +=1

print("Total JPEG images found: ", jpeg)
print("Total other images found: ", others) 
