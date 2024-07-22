from utils import Convolution, utils, Kernels
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
import math

con = Convolution()
ut = utils()
kr = Kernels()

# Task3-1. Image Pyramids
class pyramid:
    def _reduce(self, image):
        reduced_image = image[::2, ::2]
        return reduced_image

    def _expand(self, image):
        h, w = image.shape
        expanded_image = np.zero((h * 2, w * 2), dtype=image.dtype)
        expanded_image[::2, ::2] = image
        return expanded_image

    def gaussian_pyramid(self, image, levels):
        pyramid = [image]
        for _ in range(levels - 1):
            image = con.convolution2d(image, kr.gk)
            image = self._reduce(image)
            pyramid.append(image)
        return pyramid

# Task3-2. Edge Detection
class edge_detection:
    def gradient(self, image):
        Gx = cv.filter2D(image, -1, kr.sx)
        Gy = cv.filter2D(image, -1, kr.sx)
        mag = np.sqrt(Gx**2 + Gy**2)
        phase = np.arctan2(Gx, Gy) * 180 / np.pi
        ut.compareImgs2(mag, phase, "Mag", "Phase")
        return mag, phase

    def non_maximum_suppression(self, mag, phase):
        h,w = mag.shape
        non_max_suppression = np.zeros_like(mag)
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                angle = phase[i, j]
                if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                    q, r = mag[i, j + 1], mag[i, j - 1]
                elif 22.5 <= angle < 67.5:
                    q, r = mag[i + 1, j - 1], mag[i - 1, j + 1]
                elif 67.5 <= angle < 112.5:
                    q, r = mag[i + 1, j], mag[i - 1, j]
                else:
                    q, r = mag[i - 1, j - 1], mag[i + 1, j + 1]

                if mag[i, j] >= q and mag[i, j] >= r:
                    non_max_suppression[i, j] = mag[i, j]
        ut.compareImgs2(mag, non_max_suppression, "Mag", "Non max suppression")
        return non_max_suppression

    def hysteresis_thresholding(self, image, low, high):
        edge_points = np.zeros_like(image)
        h, w = image.shape
        strong_edges = (image >= high)
        weak_edges = (image >= low) & (image < high)

        # Find weak edge pixels that are connected to strong edge pixels
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if strong_edges[i, j]:
                    edge_points[i, j] = 255
                    for x in range(max(0, i - 1), min(i + 2, h)):
                        for y in range(max(0, j - 1), min(j + 2, w)):
                            if weak_edges[x, y] and edge_points[x, y]:
                                edge_points[x, y] = 255
        return edge_points

    def canney_edge_detector(self, image, low=50, high=100):
        mag, phase = self.gradient(image)
        non_max = self.non_maximum_suppression(mag, phase)
        canny_edges = self.hysteresis_thresholding(non_max, low, high)
        ut.compareImgs2(image, canny_edges, "Input", "Edges")
        return canny_edges

# Task3-3. Blob Detection
class blob_detection:
    def blob_detectiong(self, image, threshold=30):
        # Apply Gaussian blur
        blurred_image = cv.GaussianBlur(image, (5, 5), 0)

        laplacian = cv.Laplacian(blurred_image, cv.CV_64F)

        rows, cols = laplacian.shape
        zero_crossings = np.zeros_like(laplacian)
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if laplacian[i, j] * laplacian[i - 1, j] < 0 or laplacian[i, j - 1] < 0:
                    zero_crossings[i,j] = 255

        blobs = np.zeros_like(zero_crossings)
        blobs[zero_crossings < threshold] = 255

        return blobs

# Task3-4. Line Detection
class line_detection:
    def hough_transform(self, image):
        rows, cols = image.shape
        max_distance = int(math.sqrt(rows ** 2 + cols ** 2))
        accumulator = np.zeros((max_distance * 2, 180), dtype=np.uint8)

        # Detect edges using Canny edge detection
        edges = cv.Canny(image, 50, 150)
        for y in range(rows):
            for x in range(cols):
                if edges[y][x] > 0:
                    for theta in range(0, 180):
                        rho = int(x * math.cos(math.radians(theta)) + y * math.sin(math.radians(theta)))
                        accumulator[rho][theta] += 1
        return accumulator

    def _lines(self, accumulator, threshold=180):
        # Find lines from accumulator
        lines = []
        for rho in range(accumulator.shape[0]):
            for theta in range(accumulator.shape[1]):
                if accumulator[rho][theta] > threshold:
                    a = np.cos(math.radians(theta))
                    b = np.sin(math.radians(theta))
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + 1000 * (-b))
                    y1 = int(y0 + 1000 * (a))
                    x2 = int(x0 - 1000 * (-b))
                    y2 = int(y0 - 1000 * (a))
                    lines.append(((x1, y1), (x2, y2)))
        return lines

    def detect_lines(self, image, threshold=100):
        accumulator = self.hough_transform(image)
        lines = self._lines(accumulator, threshold)
        for line in lines:
            cv.line(image, line[0], line[1], (0, 255, 0), 2)

        cv.imshow("Detected Lines", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def detect_line(self, image_path, threshold=100):
        image = cv.imread(image_path)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (5, 5), 0)
        canny = cv.Canny(blurred, 50, 150)
        lines = cv.HoughLinesP(canny, 1, np.pi / 180, threshold, minLineLength=100, maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        ut.imShow(image)
        # cv.imshow("Detected Lines", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

# Task3-5. Corner Detection
class corner_detection:
    def calculate_gradients(self, image):
        Gx = cv.filter2D(image, -1, kr.sx)
        Gy = cv.filter2D(image, -1, kr.sy)
        return Gx, Gy

    def structure_tensor(self, G_x, G_y):
        Ixx = G_x ** 2
        Iyy = G_y ** 2
        Ixy = G_x * G_y
        return Ixx, Iyy, Ixy

    def corner_response(self, Ixx, Iyy, Ixy, k=0.04):
        determinant = (Ixx * Iyy) - (Ixy ** 2)
        trace = Ixx + Iyy
        corner_response = determinant - k * (trace ** 2)
        return corner_response

    def non_maximum_suppression(self, corner_response, size = 5):
        radius = size // 2
        h, w = corner_response.shape
        suppressed_response = np.zeros_like(corner_response)

        for i in range(radius, h - radius):
            for j in range(radius, w - radius):
                local_max = np.amax(corner_response[i - radius:i + radius + 1, j - radius: j + radius + 1])
                if corner_response[i, j] == local_max:
                    suppressed_response[i, j] = corner_response[i, j]

        return suppressed_response

    def detect_corners(self, image, threshold=0.1, size=5, k=0.04):
        # Calculate
        G_x, G_y = self.calculate_gradients(image)

        Ixx, Iyy, Ixy = self.structure_tensor(G_x, G_y)

        # Calculate corner response
        corner_response = self.corner_response(Ixx, Iyy, Ixy, k)

        # Non-maximum suppression
        corner_response = self.non_maximum_suppression(corner_response, size)

        corners = np.zeros_like(corner_response)
        corners[corner_response > threshold] = 255
        ut.compareImgs2(image, corners, "Image", "Corners")
        return corners




