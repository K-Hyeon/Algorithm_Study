from Lab07 import pyramid, edge_detection, corner_detection, blob_detection, line_detection
from utils import Convolution, utils, Kernels
import numpy as np
import cv2 as cv

input1 = './data/cameraman.tif'
input2 = './data/clutter1.bmp'
input3 = './data/foggysf1.jpg'
input4 = './data/foggysf2.jpg'
input5 = './data/toysflash.png'
input6 = './data/toysnoflash.png'
savepath = './data/bimg1.jpg'
flag = 0

con = Convolution()
ut = utils()
kr = Kernels()
pm = pyramid()
ed = edge_detection()
cd = corner_detection()
bd = blob_detection()
ld = line_detection()

def main():
    img = ut.imRead(input2, 0)
    img2 = ut.imRead(input1, 0)

    # Task3-1. Image Pyramids
    # gp = pm.gaussian_pyramid(img, levels=3)
    # for i in range(len(gp)):
    #     print(gp[i].shape)
    #     ut.imShow(gp[i].astype(np.uint8), 'Gaussian Level ' + str(i))

    # Task3-2. Edge Detection
    # ce = ed.canney_edge_detector(img, 50, 100)
    #ut.imShow(cv.Canny(img, 50, 100))

    # Task3-3. Blob Detection
    # ut.imShow(bd.blob_detectiong(img, 30))

    # Task3-4. Line Detection
    # ld.detect_lines(img, 50)
    # ld.detect_line(input1)

    # Task3-5. Corner Detection
    # ut.imShow(cd.detect_corners(img2, 3, 3, 0.05))
    # ut.imShow(cv.cornerHarris(img2, 3, 15, 0.04))
    # ut.compareImgs2(img2, cv.cornerHarris(img2, 3, 15, 0.04), "Original", "Corner Harris")

if __name__ == '__main__':
    main()


