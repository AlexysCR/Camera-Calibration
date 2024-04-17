import cv2
import argparse

def extractImages(pathIn, pathOut):
	vidcap = cv2.VideoCapture(pathIn)
	success,image = vidcap.read()
	count = 0
	while success:
		cv2.imwrite(pathOut + "frame%d.jpg" % count, image)     # save frame as JPEG file
		success,image = vidcap.read()
		print('Read a new frame: ', count)
		count += 1

if __name__=="__main__":
	a = argparse.ArgumentParser()
	a.add_argument("--pathIn", help="path to video", default="video_new.h264")
	a.add_argument("--pathOut", help="path to images", default = "frames")
	args = a.parse_args()
	print(args)
	extractImages(args.pathIn, args.pathOut)