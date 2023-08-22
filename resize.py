import cv2 
import argparse
import os
import shutil

parser = argparse.ArgumentParser(
    prog="Image Resizer",
    description="Resizes Images based on input",
)

parser.add_argument("-f", "--folder",help="image folder path")
parser.add_argument("-C", "--copy_directory", help="Copy Directory")
parser.add_argument("-R","--reduce_percentage", help="reduce to percentage")
args = parser.parse_args()

sourceFolder = args.folder
copyDir = args.copy_directory
percentage = float(args.reduce_percentage)

if not os.path.exists(copyDir):
    os.mkdir(copyDir)

for f in os.listdir(sourceFolder):
    nameFile = os.path.join(sourceFolder, f)
    if nameFile.lower().endswith(('.png', '.jpg')):
        copyPath = os.path.join(copyDir, f)
        shutil.copyfile(nameFile, copyPath)
        img = cv2.imread(copyPath)
        x = int(img.shape[0] * percentage)
        y = int(img.shape[1] * percentage)
        cv2.resize(img, (x,y))
