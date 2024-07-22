import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys


class Kernels:
    gk=np.array([[1, 4, 6, 4, 1],
              [4, 16, 24, 16, 4],
              [6, 24, 36, 24, 6],
              [4, 16, 24, 16, 4],
              [1, 4, 6, 4, 1]]) / 256.0

    # Laplacian Operator
    Lapx = np.array([[0, 0, 0],
                   [1, -2, 1],
                   [0, 0, 0]], dtype=np.float32)
    Lapy = np.array([[0, 1, 0],
                     [0, -2, 0],
                     [0, 1, 0]], dtype=np.float32)
    Lapxy = np.array([[0, 1, 0],
                     [1, -4, 1],
                     [0, 1, 0]], dtype=np.float32)

    sy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]], dtype=np.float32)
    # Sobel operators
    sx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
    sy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]], dtype=np.float32)

    def gaussian_kernel2d(self,size, sigma):
        if size % 2 == 0:
            raise ValueError("Kernel size must be odd")
        grid = np.arange(-size // 2 + 1, size // 2 + 1)
        x, y = np.meshgrid(grid, grid)
        kernel = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
        kernel /= np.sum(kernel)
        return kernel
class Convolution:

    def con1Test(self):
        signal = np.random.randint(1, 100, size=50)
        kernel = np.array([1, 0, -1])

        # Perform 1D convolution
        result = self.convolution1d(signal, kernel)
        # Plot original signal
        plt.subplot(2, 1, 1)
        plt.plot(signal, label='Original Signal')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Original Signal')
        plt.legend()

        # Plot convolved signal
        plt.subplot(2, 1, 2)
        plt.plot(result, label='Convolved Signal', color='orange')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Convolved Signal')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def convolution1d(self,signal, kernel):
        l = len(signal)
        k = len(kernel)

        # Calculate padding size
        pad_size = k // 2

        # Create zero-padded signal
        padded_signal = np.pad(signal, pad_size, mode='constant')

        # Initialize output signal
        output = np.zeros(l)

        # Perform convolution
        for i in range(l):
            win = padded_signal[i:i + k]
            output[i] = np.sum(win * kernel)

        return output

    def convolution2d(self, image, kernel):
        ut=utils()
        h, w = image.shape
        k1, k2 = kernel.shape

        # Calculate padding size
        pad_height = k1 // 2
        pad_width = k2 // 2

        padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

        # Initialize output image
        output = np.zeros_like(image)

        # Perform convolution
        for i in range(h):
            for j in range(w):
                win = padded_image[i:i + k1, j:j + k2]
                output[i, j] = np.sum(win * kernel)
        ut.compareImgs2(image, output, t1="Orinal Image", t2="Filtered Image")
        return output
class utils:

    def threshold(self, img, th=127):
        bimg = img.copy()
        h, w = img.shape
        for i in range(h):
            for j in range(w):
                if img[i, j] <= th:
                    bimg[i, j] = 0
                else:
                    bimg[i, j] = 1
        return bimg

    def padd_img(self,img, pad_size):
        h, w = img.shape
        padded_img = np.zeros((h + 2 * pad_size, w + 2 * pad_size))
        padded_img[pad_size:-pad_size, pad_size:-pad_size] = img
        return padded_img

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

    def compareImgs2(self, img1, img2, t1="Input", t2="Output"):
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

    def show_images(images, titles=None, figsize=(15, 6), cmap='gray'):
        cols = 4
        rows = (len(images) % cols) + 1
        num_images = len(images)
        if titles is not None and len(titles) != num_images:
            raise ValueError("Number of titles should match the number of images.")

        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        axes = axes.ravel()

        for i, ax in enumerate(axes):
            if i < num_images:
                ax.imshow(images[i], cmap=cmap)
                ax.axis('off')
                ax.set_title(titles[i])
            else:
                ax.axis('off')  # Turn off unused axes

        plt.tight_layout()
        plt.show()

    def plot_multiple(imgs, num_img, main_title='', titles=''):
        rows = (num_img + 1) / 2
        plt.figure()
        plt.title(main_title)
        f, axarr = plt.subplots(rows, 2)
        for i, (img, title) in enumerate(zip(imgs, titles)):
            axarr[i / 2, i % 2].imshow(img.astype(np.uint8), cmap='gray')
            axarr[i / 2, i % 2].set_title(title)
        plt.waitforbuttonpress()

