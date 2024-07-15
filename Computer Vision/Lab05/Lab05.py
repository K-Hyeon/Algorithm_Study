import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys

# Task1
class Convolution:
    def test_conv2d(self):
        signal = np.array([[1, 5, 6, 7, 5],
                           [11, 15, 16, 17, 15],
                           [10, 50, 60, 70, 50]])
        kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) * (1 / 9)

        output = self.conv2D(signal, kernel)
        print(signal)
        print(kernel)
        print(output)

    def conv2D(self, image, kernel):
        h, w = image.shape
        k1, k2 = kernel.shape
        hw1 = k1 // 2
        hw2 = k1 // 2
        padded_image = np.pad(image, [(hw1, hw2), (hw1, hw2)], mode="constant")
        output = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                win = padded_image[i:i+k1, j:j+k2] # window
                output[i, j] = np.sum(win * kernel)
        return output

    def test_conv1d(self):
        # signal = np.random.randint(1, 100, 50)
        # kernel = np.array([1, 0, -1])
        signal = np.array([1, 5, 6, 7])
        kernel = np.array([1, 2, 1]) * (1 / 4)

        output = self.conv1D(signal, kernel)
        print(signal)
        print(kernel)
        print(output)

    def conv1D(self, signal, kernel):
        l = len(signal)
        k = len(kernel)
        psize = k // 2
        padded_signal = np.pad(signal, psize, mode="constant")
        output = np.zeros(l)
        for i in range(l):
            win = padded_signal[i:i+k] # window
            output[i] = np.sum(win * kernel)
        return output

# Task2
class LinearFiltering:
    def box_filter2(self, image, size):
        S = self.integral_image(image)
        output = S[size:,size:] + S[:-size,:-size] - S[:-size,size:] - S[size:,:-size]
        output = output/(size*size)
        return output.astype(np.uint8)

    def integral_image(self, image):
        h, w = image.shape
        S = np.zeros_like(image, dtype='int')
        S[0, 0] = image[0, 0]
        for i in range(1, h):
            S[i, 0] = S[i-1, 0] + image[i, 0]
        for i in range(1, w):
            S[0, i] = S[0, i-1] + image[0, i]

        for i in range(1, h):
            for j in range(1, w):
                S[i, j] = image[i, j] + S[i-1, j] + S[i, j-1] - S[i-1, j-1]

        return S

# Task4
class Kernels:
    Prewittx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    Prewitty = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    Sobelx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    Sobely = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    Scharrx = np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]])
    Scharry = np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]])

    L0 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    def gauss2D(self, size, sigma):
        if size % 2 == 0:
            raise ValueError("Kernel size should be odd number")
        grid = np.arange(-size // 2 + 1, size // 2 + 1)
        x, y = np.meshgrid(grid, grid)
        kernel = np.exp(-(x**2 + y**2)/(2 * sigma**2))
        kernel = kernel / sum(kernel)
        return kernel

    def gauss1D(self, size, sigma):
        x = (np.arrange(size) - size // 2)
        kernel = np.exp(-x ** 2/(2 * sigma**2))
        kernel = kernel/sum(kernel)
        return kernel

    def box_kernel(self, size):
        if size % 2 == 0:
            raise ValueError("Kernel size should be odd number")
        kernel = np.ones((size, size), dtype=float)
        norm_factor = size * size # normalizaion_factor
        kernel = kernel / norm_factor
        return kernel

    def box_kernel_x(self, size):
        if size % 2 == 0:
            raise ValueError("Kernel size should be odd number")
        kernel = np.ones((1, size), dtype=float)
        kernel = kernel / size
        return kernel

    def box_kernel_y(self, size):
        if size % 2 == 0:
            raise ValueError("Kernel size should be odd number")
        kernel = np.ones((size, 1), dtype=float)
        kernel = kernel / size
        return kernel

class utils:
    def binarize(self, img, th=127):
        ut = utils()
        hist, _ = ut.imHist(img)
        if th == 127:
            th = ut.findTh(hist)

        bimg = img.copy()
        h, w = img.shape
        for i in range(h):
            for j in range(w):
                if img[i, j] <= th:
                    bimg[i, j] = 0
                else:
                    bimg[i, j] = 1
        return bimg

    def findTh(self, hist):
        k = 256
        threshold = int(k / 2)
        lastexpected1 = lastexpected2 = 0

        while True:
            expected1 = expected2 = 0
            t_exp1 = sum(hist[:threshold])
            t_exp2 = sum(hist[threshold:])
            for i in range(threshold):
                expected1 += (hist[i] / t_exp1) * i

            for i in range(threshold, k):
                expected2 += (hist[i] / t_exp2) * i

            threshold = (expected1 + expected2) / 2
            if abs(expected1 - lastexpected1) != 0 and abs(expected2 - lastexpected2) != 0:
                break
            lastexpected1 = expected1
            lastexpected2 = expected2
            # print(expected2, expected1)
        return threshold

    def imHist(self, img):
        h, w = img.shape
        hist = np.zeros([256], np.int32)
        # calculate histogram
        for i in range(0, h):
            for j in range(0, w):
                hist[img[i, j]] += 1
        pdf = hist / (h * w)
        return hist, pdf

    def imRead(self, input, flag):
        img = cv.imread(input, flag)
        if img is None:
            sys.exit("Could not read the image.")
        print(img.shape)
        return img

    def imWrite(self, img, path):
        if img is None:
            sys.exit("Not a valid image object.")
        cv.imwrite(path, img)

    def imShow(self, img, title="Output"):
        if img is None:
            sys.exit("Not a valid image object.")

        if len(img.shape) == 2:
            plt.title(title)
            plt.imshow(img, cmap='gray')
        else:
            plt.title(title)
            plt.imshow(img)
        plt.show()

    def compareImgs(self, img1, img2, t1="Orinal Image", t2="Transformed Image"):
        # plot
        fig = plt.figure()

        a1 = fig.add_subplot(1, 2, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(1, 2, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        fig.tight_layout()
        plt.show()

    def compareImgs6(self, img1, img2, img3, img4, img5, img6, t1="Orinal Image", t2="Output1", t3="Output2", t4="Output3", t5="Output4", t6="Output5"):
        # plot
        fig = plt.figure()

        a1 = fig.add_subplot(2, 3, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(2, 3, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        a3 = fig.add_subplot(2, 3, 3)
        a3.imshow(img3, cmap='gray')
        a3.set_title(t3)

        a4 = fig.add_subplot(2, 3, 4)
        a4.imshow(img4, cmap='gray')
        a4.set_title(t4)

        a5 = fig.add_subplot(2, 3, 5)
        a5.imshow(img5, cmap='gray')
        a5.set_title(t5)

        a6 = fig.add_subplot(2, 3, 6)
        a6.imshow(img6, cmap='gray')
        a6.set_title(t6)

        fig.tight_layout()
        plt.show()
