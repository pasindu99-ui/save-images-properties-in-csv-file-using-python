# Required Libraries
from os import listdir
from os.path import isfile, join
from pathlib import Path
import numpy
import cv2
import argparse
import numpy
import csv

# Check whether the CSV
# exists or not if not then create one.
my_file = Path("csv\details.csv")

if my_file.is_file():
	f = open(my_file, "w+")
	with open('csv\details.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		
		writer.writerow(["S.No.", "Name", "low withered poor","low withered best", "low withered below best","low fresh poor", "low fresh best","low fresh below best"])
	f.close()
	pass
	
else:
	with open('csv\details.csv', 'w', newline = '') as file:
		writer = csv.writer(file)
		
		writer.writerow(["S.No.", "Name", "low withered poor","low withered best", "low withered below best","low fresh poor", "low fresh best","low fresh below best"])

# Argparse function to get
# the path of the image directory
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image",required = True,help = "Path to folder")

args = vars(ap.parse_args())

# Program to find the
# colors and embed in the CSV
mypath = args["image"]

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype = object)

for n in range(0, len(onlyfiles)):
	
	path = join(mypath,onlyfiles[n])
	images[n] = cv2.imread(join(mypath,onlyfiles[n]),cv2.IMREAD_UNCHANGED)
	
	img = cv2.imread(path)
	h,w,c = img.shape
	print(h, w, c)
	
	avg_color_per_row = numpy.average(img, axis = 0)
	avg_color = numpy.average(avg_color_per_row, axis = 0)
	
	with open('csv/details.csv', 'a', newline = '') as file:
		writer = csv.writer(file)
		writer.writerow([n+1, onlyfiles[n],0,0,0,0,0,0])
		file.close()
