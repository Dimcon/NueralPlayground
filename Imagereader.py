

def importdata(filename, imagecount):
	pixels = []
	magicnum = 0
	numimages = 0
	rows = 0
	cols = 0
	images = []
	class tmp:
		pass
	with open(filename, "rb") as inputfile:
		# inputbytes = inputfile.read()
		import os
		filesize = os.path.getsize(filename)
		magicnum = int.from_bytes(inputfile.read(4), byteorder='big')
		numimages = int.from_bytes(inputfile.read(4), byteorder='big')
		rows = int.from_bytes(inputfile.read(4), byteorder='big')
		cols = int.from_bytes(inputfile.read(4), byteorder='big')
		for i in range(13, filesize):
			color = inputfile.read(1)
			color = int.from_bytes(color,byteorder='big')
			pixels.append(color)
	imagesize = len(pixels) / int(numimages)
	numimages = imagecount
	icount = 0
	print(numimages)
	for i in range(numimages):
		images.append(tmp())
		images[i].pixels = []
		images[i].cols = cols
		images[i].rows = rows
		for j in range(int(imagesize)):
			images[i].pixels.append(pixels[icount])
			icount += 1
	return images

