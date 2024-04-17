import numpy as np
import cv2 as cv
import glob
import os
from matplotlib import pyplot as plt

# Initial Parameters
chessGrid = (7,7)
frameSize = (1920,1080)
saveDirectory = "FramesCalibrated"  #Directory where images are saved

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessGrid[0]*chessGrid[1],3), np.float32)
objp[:,:2] = np.mgrid[0:chessGrid[0],0:chessGrid[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Frame Counting
TotalFrames = 0
dir = "FramesNew"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        TotalFrames += 1
print("\nTotal Frames:",TotalFrames)

#Frame Selection
increment = 30
print("Selecting every", increment, "frames --- (Increment =", increment,") ---\n")
FramesToSel = int(TotalFrames/increment)
percent = round(FramesToSel/TotalFrames*100,2)
print("Selecting ", percent,"%  of the total frames")

numFrame = 0
imageCounter = 0
images = list()

for i in range(FramesToSel):
    fileName = 'FramesNew/.frame' + str(numFrame) + '.jpg'
    images = images + glob.glob(fileName)
    numFrame += increment
    imageCounter += 1

print("Images to analize:",imageCounter,"\n")


imgPatternCounter = 0
print("Starting to look for  (",chessGrid[0],"x",chessGrid[1],")  chess grid...")

for fname in images:

    #Reading image and applying gray filter
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ret, corners = cv.findChessboardCorners(gray, chessGrid, None)
    ''''''''''''''
    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        imgPatternCounter += 1
        cv.drawChessboardCorners(img, chessGrid, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1)

cv.destroyAllWindows()

print("Image with detected Chessboard:", imgPatternCounter)

print("------------------------------------------------------------")

# Camera Calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
print("\nCamera Calibrated:",ret)
print("\nCamera Matrix:\n",mtx)
print("\nDistortion Parameters:",dist)
print("\nRotation Vectors:\n",rvecs)
print("\nTraslation Vectors:\n",tvecs)

print("------------------------------------------------------------\n")

# Re-projection Error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "Total Error: {}".format(mean_error/len(objpoints)) )


# Undistortion
# This frames were manually selected due to the different positions in the recording
frames = ['FramesNew/.frame0.jpg','FramesNew/.frame400.jpg','FramesNew/.frame700.jpg','FramesNew/.frame1200.jpg','FramesNew/.frame1500.jpg',
          'FramesNew/.frame1750.jpg','FramesNew/.frame1900.jpg','FramesNew/.frame2000.jpg','FramesNew/.frame2200.jpg','FramesNew/.frame2300.jpg']
frameCounter = 0

for frame in frames:

    #Reading Image and finding new camera matrix
    img = cv.imread(frame)

    if frameCounter == 0:
        h, w = img.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        print("\nNew Camera Matrix:\n", newcameramtx)
        print("\nROI:", roi)

    # USING UNDISTOR
    # undistort
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    undistorFrame = dst[y:y+h, x:x+w]
    # Saving image in save directory
    os.chdir(saveDirectory)
    fileName = "resUndistor" + str(frameCounter) + ".jpg"
    cv.imwrite(fileName, undistorFrame)
    os.chdir("..")

    # USING REMAPPING
    # undistort
    mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
    dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
    # crop the image
    x, y, w, h = roi
    remappFrame = dst[y:y+h, x:x+w]
    # Saving image in save directory
    os.chdir(saveDirectory)
    fileName ='resRemapp' + str(frameCounter) + ".jpg"
    cv.imwrite(fileName, remappFrame)
    os.chdir("..")

    #Generating plot to show images
    fig = plt.figure(figsize=(12, 10))
    fig.tight_layout()
    rows = 1
    columns = 3

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title("Original Frame")

    fig.add_subplot(rows, columns, 2)
    plt.imshow(remappFrame)
    plt.axis('off')
    plt.title("Remapped Frame")

    fig.add_subplot(rows, columns, 3)
    plt.imshow(undistorFrame)
    plt.axis('off')
    plt.title("Undistorted Frame")

    plt.subplots_adjust(left=0.01, bottom=None, right=0.99, top=None, wspace=0.014, hspace=None)
    plt.show()
    frameCounter += 1