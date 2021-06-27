import PIL.Image
import glob
import os

if not "converted" in os.listdir():
	os.mkdir("converted")

lst_imgs = [i for i in glob.glob("*.jpg")]
print(lst_imgs)

for i in lst_imgs:
	img = PIL.Image.open(i)
	img = img.convert("RGB")
	img.save("converted\\"+i, "JPEG")


print("Done.")
os.startfile("converted")