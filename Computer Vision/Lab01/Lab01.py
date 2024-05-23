import cv2 as cv
import sys
import matplotlib.pyplot as plt

class Lab01:
    # task1
    def task_flip(self, img):
        flip_image = img[::-1]
        print(flip_image)
        self.compareIms(img, flip_image, t2 = "Flip")

    def task_flop(self, img):
        flop_image = []
        for row in img:
            flop_image.append(row[::-1])
        print(flop_image)
        self.compareIms(img, flop_image, t2 = "Flop")

    def task_flip_flop(self, img):
        flip_flop_image = []
        for row in img:
            flip_flop_image.append(row[::-1])
        flip_flop_image = flip_flop_image[::-1]
        print(flip_flop_image)
        self.compareIms(img, flip_flop_image, t2 = "Flip-Flop")

    def task_invert(self, img):
        invert_image = []
        for row in img:
            invert_row = [255 - pixel for pixel in row]
            invert_image.append(invert_row)
        print(invert_image)
        self.compareIms(img, invert_image, t2 = "Invert")

    def task_rotate90(self, img):
        rotated_image = []
        for i in range(len(img[0])):
            rotated_row = [row[i] for row in reversed(img)]
            rotated_image.append(rotated_row)
        print(rotated_image)
        self.compareIms(img, rotated_image, t2 = "Rotate")

    # task2
    def task2_sum(self, img1, img2):
        sum_img = []
        for i in range(4):
            sum_row = []
            for j in range(4):
                sum_pixel = min(img1[i][j] + img2[i][j], 255)
                sum_row.append(sum_pixel)
            sum_img.append(sum_row)
        print(sum_img)
        self.task2_compareIms(img1, img2, sum_img, t3 = "Sum Image")

    def task2_difference(self, img1, img2):
        difference_img = []
        for i in range(len(img1)):
            difference_row = []
            for j in range(len(img1[i])):
                difference_pixel = max(img1[i][j] - img2[i][j], 0)
                difference_row.append(difference_pixel)
            difference_img.append(difference_row)
        print(difference_img)
        self.task2_compareIms(img1, img2, difference_img, t3 = "Difference Image")

    def task2_Absolute_Difference(self, img1, img2):
        absolute_difference_img = []
        for i in range(4):
            absolute_difference_row = []
            for j in range(4):
                sum_pixel = min(abs(img1[i][j] - img2[i][j]), 255)
                absolute_difference_row.append(sum_pixel)
            absolute_difference_img.append(absolute_difference_row)
        print(absolute_difference_img)
        self.task2_compareIms(img1, img2, absolute_difference_img, t3 = "Absolute Difference Image")

    def task2_compareIms(self, img1, img2, transformed, t1 = "Orignal1", t2 = "Orignal2", t3 = "Transformed"):
        fig = plt.figure()
        a1 = fig.add_subplot(1, 3, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(1, 3, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        a3 = fig.add_subplot(1, 3, 3)
        a3.imshow(transformed, cmap='gray')
        a3.set_title(t3)

        fig.tight_layout()
        plt.show()

    # task3
    def Horizontal_flip(self, img):
        horizontal_fliped = img[::-1, :]
        self.compareIms(img, horizontal_fliped, t2="Horizontal Flip")

    def Vertical_flip(self, img):
        vertical_fliped = img[:, ::-1]
        self.compareIms(img, vertical_fliped, t2="Vertical Flip")

    def HV_flip(self, img):
        HV_fliped = img[::-1, ::-1]
        self.compareIms(img, HV_fliped, t2 = "Horizontal and Vertical Flips")

    def rotate(self, img, angle):
        (h, w) = img.shape[:2]
        center = (w//2, h//2)

        # Calculate the rotation matrix
        matrix = cv.getRotationMatrix2D(center, -angle, 1.0)

        # image rotation
        rotated = cv.warpAffine(img, matrix, (w, h))

        self.compareIms(img, rotated, t2="Rotate {}".format(int(angle)))

    def Resize(self, img, width = None, height = None):
        if width is None and height is None:
            raise ValueError("Either width or height must be specified...")

        resized_image = cv.resize(img, (width, height))
        self.compareIms(img, resized_image, t2="Resize ({}, {})".format(width, height))

    def gray_Contrast_enhancement(self, img):
        equalized_image = cv.equalizeHist(img)
        self.compareIms(img, equalized_image, t2 = "Contrast enhancement")

    def rgb_Contrast_enhancement(self, img):
        # Disconnect the BGR channel
        b, g, r = cv.split(img)

        # Apply histogram smoothing for each channel
        b_equalized = cv.equalizeHist(b)
        g_equalized = cv.equalizeHist(g)
        r_equalized = cv.equalizeHist(r)

        # Put the channels back together
        equalized_img = cv.merge((b_equalized, g_equalized, r_equalized))
        self.compareIms(img, equalized_img, t2 = "Contrast enhancement")

    def compareIms(self, orignal, transformed, t1 = "Orignal", t2 = "Transformed"):
        fig = plt.figure()
        a1 = fig.add_subplot(1, 2, 1)
        # a2.imshow(orignal, cmap='gray')
        a1.imshow(cv.cvtColor(orignal, cv.COLOR_RGB2BGR))
        a1.set_title(t1)

        a2 = fig.add_subplot(1, 2, 2)
        #a2.imshow(transformed, cmap='gray')
        a2.imshow(cv.cvtColor(transformed, cv.COLOR_RGB2BGR))
        a2.set_title(t2)
        fig.tight_layout()
        plt.show()

    def imRead(self, fname, mode):
        img = cv.imread(fname, mode)

        if img is None:
            sys.exit("Could not read the image file...")

        #print(img)
        print(img.shape)

        return img

    def imShow(self, iimg):
        cv.imshow("My Image", iimg)
        cv.waitKey(0)
        cv.destroyAllWindows()
