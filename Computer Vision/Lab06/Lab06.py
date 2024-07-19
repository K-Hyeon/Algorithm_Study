import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
import math
from functools import partial, reduce


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


ut = utils()

# Task1
class noisy_image:
    def Gaussian_noise(self, image, mean=0, sigma=0.01):
        h, w = image.shape
        image = image / 255
        nimage = np.copy(image)
        gauss = np.random.normal(mean, sigma**.5, (h,w))
        nimage = image + gauss
        nimage = np.clip(nimage, 0, 1)
        nimage = np.uint8(nimage * 255)
        ut.compareImgs(image, nimage, "Orignal", " Gaussian Noisy")
        return nimage

    def salt_pepper_noise(self, image, saltP = 0.01, pepperP= 0.1):
        h, w = image.shape
        nimage = np.copy(image)
        salt_noise = np.random.rand(h, w)
        nimage[salt_noise < saltP] = 255
        pepper_noise = np.random.rand(h, w)
        nimage[pepper_noise < pepperP] = 0
        ut.compareImgs(image, nimage, "Orignal", "Salt pepper Noisy")
        return nimage

class measure:
    def PSNR(self, A, B):
        mse = self.MSE(A, B)
        psnr = 10 * np.log10((255**2) / mse)
        return psnr


    def MSE(self, A, B):
        h, w = A.shape
        mse = 0
        for i in range(h):
            for j in range(w):
                mse += ((float(A[i, j]) - float(B[i, j]))**2)
        mse /= (h*w)
        return mse

# Task2
class nan_linear_filtering:
    def gaussian_kernel(self, x, sigma):
        return np.exp(-(x ** 2) / (2 * sigma ** 2))

    def mean_shift_filter(self, image, spatial_radius, color_radius, num_iterations=3):
        # Get image shape and size
        height, width = image.shape
        oimg = np.copy(image)
        # Convert image to float for accurate calculations
        image = image.astype(np.float64)

        # Iterate mean shift algorithm
        for _ in range(num_iterations):
            # Create an empty image for the updated values
            updated_image = np.zeros_like(image)

            # Iterate through each pixel
            for y in range(height):
                for x in range(width):
                    # Get the spatial window
                    y_min = max(0, y - spatial_radius)
                    y_max = min(height, y + spatial_radius + 1)
                    x_min = max(0, x - spatial_radius)
                    x_max = min(width, x + spatial_radius + 1)
                    spatial_window = image[y_min:y_max, x_min:x_max]

                    # Calculate color weights
                    color_diff = spatial_window - image[y, x]
                    color_distances = np.abs(color_diff)
                    color_weights = self.gaussian_kernel(color_distances, color_radius)

                    # Calculate mean shift vector
                    mean_shift = (color_weights * color_diff).sum() / color_weights.sum()

                    # Update pixel value
                    updated_image[y, x] = image[y, x] + mean_shift

            # Update the original image with the updated values
            image = updated_image

        # Clip and convert image back to uint8 format
        updated_image = np.clip(image, 0, 255).astype(np.uint8)
        #ut.compareImgs(oimg, updated_image)
        return updated_image

    def anisotropic_diffusion(self, image, iterations, delta_t, kappa):
        image = image.astype(np.float32)
        result = np.copy(image)
        # Get image dimensions
        rows, cols = image.shape
        weight_N = weight_S = weight_E = weight_W = 1.0

        for _ in range(iterations):
            # Calculate the gradients using central differences
            delta_N = np.roll(result, -1, axis=0) - result
            delta_S = np.roll(result, 1, axis=0) - result
            delta_E = np.roll(result, -1, axis=1) - result
            delta_W = np.roll(result, 1, axis=1) - result

            # Calculate the diffusion coefficients
            c_N = np.exp(-np.square(delta_N / kappa))
            c_S = np.exp(-np.square(delta_S / kappa))
            c_E = np.exp(-np.square(delta_E / kappa))
            c_W = np.exp(-np.square(delta_W / kappa))

            # Update the image using finite difference scheme
            result += delta_t * (
                    weight_N * delta_N * c_N +
                    weight_S * delta_S * c_S +
                    weight_E * delta_E * c_E +
                    weight_W * delta_W * c_W
            )
        # ut.compareImgs(image, result, t2='Anisotropic Diffusion')
        return np.uint8(result)

    def isodiff(self, image, steps, b, lam=0.25):  # takes image input, the number of iterations,
        # image= image/255
        filtered_image = np.zeros(image.shape, dtype=image.dtype)
        for t in range(steps):
            print(t)
            dn = image[:-2, 1:-1] - image[1:-1, 1:-1]
            ds = image[2:, 1:-1] - image[1:-1, 1:-1]
            de = image[1:-1, 2:] - image[1:-1, 1:-1]
            dw = image[1:-1, :-2] - image[1:-1, 1:-1]
            filtered_image[1:-1, 1:-1] = image[1:-1, 1:-1] + \
                                         lam * (dn + ds + de + dw)
        filtered_image.astype(np.uint8)
        ut.compareImgs(image, filtered_image)
        return filtered_image

    def non_local_mean(self, image, h, ksize, swin):
        h, w = image.shape
        pw = swin // 2
        pw2 = ksize // 2
        padded_image = np.pad(image, pw, mode='constant')
        filtered_image = padded_image.copy()

        # Compare tiles in search window
        for i in range(pw, pw + h):
            for j in range(pw, pw + w):
                searchWin = padded_image[i - pw2:i + pw2 + 1, j - pw2:j + pw2 + 1]

                value = 0
                totalWeight = 0

                # Weight calculation
                for k in range(i - pw, i - pw + swin - ksize, 1):
                    for m in range(j - pw, j - pw + swin - ksize, 1):
                        # find the small box
                        ksWin = padded_image[m:m + ksize, k:k + ksize]
                        distance = np.sqrt(np.sum(np.square(ksWin - searchWin)))

                        # weight is computed as a weighted softmax over the euclidean distances
                        weight = np.exp(-distance / h)
                        totalWeight += weight
                        value += weight * padded_image[m + pw2, k + pw2]

                value /= totalWeight
                filtered_image[j, i] = value
        # ut.compareImgs(image, filtered_image)
        return filtered_image[pw:pw + h, pw:pw + h]

    def gaussian(self, x, sigma):
        return (1 / (2 * math.pi * (sigma ** 2))) * math.exp(-(x ** 2) / (2 * (sigma ** 2)))

    def bilateral_filter(self, image, diameter, sigma_color, sigma_space):
        height, width = image.shape
        filtered_image = np.zeros_like(image)

        for i in range(height):
            for j in range(width):
                pixel = 0.0
                total_weight = 0.0

                for k in range(-diameter // 2, diameter // 2 + 1):
                    for l in range(-diameter // 2, diameter // 2 + 1):
                        x = i + k
                        y = j + l

                        if x >= 0 and x < height and y >= 0 and y < width:
                            # print(abs(image[x, y] - image[i, j]))
                            intensity_diff = abs(image[x, y] - image[i, j])
                            color_weight = self.gaussian(intensity_diff, sigma_color)
                            spatial_weight = self.gaussian(math.sqrt(k ** 2 + l ** 2), sigma_space)
                            weight = color_weight * spatial_weight

                            pixel += image[x, y] * weight
                            total_weight += weight

                filtered_image[i, j] = pixel / total_weight

        # ut.compareImgs(image, filtered_image)
        return filtered_image.astype(np.uint8)

    def joint_bilateral_filter(self, image, guidance_image, diameter, sigma_color, sigma_space):
        height, width = image.shape
        filtered_image = np.zeros_like(image)

        for i in range(height):
            for j in range(width):
                pixel = 0.0
                total_weight = 0.0

                for x in range(max(0, i - diameter // 2), min(height, i + diameter // 2 + 1)):
                    for y in range(max(0, j - diameter // 2), min(width, j + diameter // 2 + 1)):
                        intensity_diff = abs(image[x, y] - image[i, j])
                        color_weight = self.gaussian(intensity_diff, sigma_color)
                        spatial_weight = self.gaussian(math.sqrt((x - i) ** 2 + (y - j) ** 2), sigma_space)
                        guidance_diff = abs(guidance_image[x, y] - guidance_image[i, j])
                        guidance_weight = self.gaussian(guidance_diff, sigma_color)
                        joint_weight = color_weight * spatial_weight * guidance_weight

                        pixel += image[x, y] * joint_weight
                        total_weight += joint_weight

                filtered_image[i, j] = pixel / total_weight

        ut.compareImgs(image, filtered_image)
        return filtered_image.astype(np.uint8)

    def median_filter(self, image, size):
        h, w = image.shape
        hw = size // 2
        padded_image = np.pad(image, hw, mode='constant')
        filtered_image = np.zeros_like(image)

        for i in range(h):
            for j in range(w):
                window = padded_image[i:i + size, j:j + size]
                filtered_image[i, j] = np.median(window)

        # ut.compareImgs(image, filtered_image, t2='Median Filter')
        return filtered_image

