import pygame

def displayimage(canvas,img, xpos,ypos,width,height):
	imagewidth = img.rows
	imageheight = img.cols
	widthmultiplier = (float(width) / float(img.cols))
	heightmultiplier = (float(height) / float(img.rows))
	count = 0
	for y in range(img.rows):
		for x in range(img.cols):
			color = (img.pixels[count], img.pixels[count], img.pixels[count])
			pygame.draw.rect(canvas, color, (
						xpos + (x * widthmultiplier),
						ypos + (y * heightmultiplier),
						widthmultiplier,
						heightmultiplier,
					), 0)
			count += 1