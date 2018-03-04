from Imagereader import *
import sys
from pygame.locals import *
from Display import *
def main():
	import pygame as pygame

	print("hello world")

	pygame.init()
	#                                    [i,[[    pixeldata    ], size     ,size      ],
	# importdata returns a dict like so: [0:[[0:0, 1:255, 2:200], 'cols':28, 'rows':28], 1:...]
	imgs = importdata("TrainingSets/Set 1/t10k-images.idx3-ubyte", 20)

	print("Found {} images".format(len(imgs)))
	print("{} pixels total".format(len(imgs[0].pixels)))
	print("{} collumns - X".format(imgs[0].cols))
	print("{} rows - Y".format(imgs[0].rows))

	import ANNObjects.Processor


	print("Starting neural network.. expect crashes...")
	import time

	start_time = time.clock()

	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[0].pixels,[28,28],255,[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[1].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[2].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[4].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	proc = ANNObjects.Processor.Processor()
	proc.doitall(imgs[3].pixels, [28, 28], 255, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	proc.Process()
	print(time.clock() - start_time, "seconds")
	print("Done")


	black = (0, 0, 0)
	white = (250, 250, 250)
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Neural playground')
	background = pygame.Surface(screen.get_size())
	background.fill(white)
	canvas = pygame.Surface(screen.get_size())

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		canvas.fill(white)
		displayimage(canvas, imgs[0],   0, 0, 200, 200)
		displayimage(canvas, imgs[1], 200, 0, 200, 200)
		screen.blit(background, (0, 0))
		screen.blit(canvas,(0, 0))
		pygame.display.flip()

if __name__ == '__main__': main()