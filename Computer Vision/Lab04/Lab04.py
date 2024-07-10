import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys

# Task1
class ConnectedComponents:
    def __init__(self, img):
        self.img = img
        self.rows = len(img)
        self.cols = len(img[0])
        self.visited = set()

    def floodfill(self, x, y, color):
        tcolor = self.img[x][y]
        queue = [(x, y)]
        components = []
        while queue:
            x, y = queue.pop(0)
            if (x, y) in self.visited:
                continue
            self.img[x][y] = color
            self.visited.add((x, y))
            components.append((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if self.isValid(nx, ny, tcolor):
                    queue.append((nx, ny))
        return components

    def isValid(self, x, y, color):
        return (0 <= x < self.rows) and (0 <= y < self.cols) and (self.img[x][y] == color) and ((x, y) not in self.visited)

    def getCC(self):
        components = []
        labled = np.zeros((self.rows, self.cols), dtype='int')
        lable = 1
        for i in range(self.rows):
            for j in range(self.cols):
                if (i ,j) not in self.visited:
                    component = self.floodfill(i, j, lable)
                    components.append(component)
                    for x, y in component:
                        labled[x][y] = lable
                    lable += 1
        return components, labled

    @staticmethod
    def cal_properties(component):
        # area
        area = len(component)

        # perimeter
        xmin = min(coord[0] for coord in component)
        ymin = min(coord[1] for coord in component)
        xmax = max(coord[0] for coord in component)
        ymax = max(coord[1] for coord in component)

        w = xmax - xmin + 1
        h = ymax - ymin + 1

        perimeter = 2 * (w + h)

        # centroid
        xsum = sum(coord[0] for coord in component)
        ysum = sum(coord[1] for coord in component)

        cx = xsum / area
        cy = ysum / area

        return {'area': area, 'perimeter': perimeter, 'centroid': (cx, cy)}

    def getProperties(self, components):
        properties = []
        for c in components:
            properties.append(self.cal_properties(c))

        for i, p in enumerate(properties):
            print(" Region = ", i + 1) # moment
            print(" Area = ", p['area']) # Area
            print(" Perimeter = ", p['perimeter']) # Perimeter
            print(" Centroid = ", p['centroid']) # Centroid
            print()
        return properties

# Task2
class TemplateMatching:
    def tmCV(self):
        image = cv.imread('./data/image1.png', 0)
        template = cv.imread('./data/template1.png', 0)

        # gray_image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        # gray_template = cv.cvtColor(template, cv.COLOR_RGB2BGR)

        dtImage = cv.distanceTransform(image, cv.DIST_L2, 5)
        dtTemplate = cv.distanceTransform(template, cv.DIST_L2, 5)
        match_result = cv.matchTemplate(dtImage, dtTemplate, cv.TM_CCOEFF_NORMED)

        return match_result

    def tempMatching(self, image, template):
        h, w = image.shape
        th, tw = template.shape

        dtImage = self.ChamferDT(image)
        dtTemplate = self.ChamferDT(template)

        #matching
        mscore = np.inf
        mloc = (0, 0)
        MM = np.zeros((h, w), dtype=np.float32)
        MM.fill(np.inf)
        for i in range(h - th + 1):
            for j in range(w - tw + 1):
                win = dtImage[i:i+th, j:j+tw]
                score = np.sum(np.abs(win - dtTemplate))
                MM[i, j] = score

            if mscore > score:
                mscore = score
                mloc = (i, j)

        return mscore, mloc, MM

    def templatematchingCV(self, image, template):
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray_template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

        # Compute distance transform
        dist_transform = cv.distanceTransform(gray_image, cv.DIST_L2, 5)
        dist_template = cv.distanceTransform(gray_template, cv.DIST_L2, 5)

        # Perform template matching
        match_result = cv.matchTemplate(dist_transform, dist_template, cv.TM_CCOEFF_NORMED)
        # best match location
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match_result)

        # Draw rectangle around the best match
        template_height, template_width = template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        cv.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

        # Display the result
        cv.imshow('Match Result', image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def ChamferDT(self, img):
        h, w = img.shape
        D = np.zeros((h, w), dtype=np.float32)
        D.fill(np.inf)

        # pass1
        for i in range(h):
            for j in range(w):
                if img[i, j] == 0:
                    D[i, j] = 0
                else:
                    if i > 0:
                        D[i, j] = min(D[i, j], D[i-1, j] + 1)
                    if j > 0:
                        D[i, j] = min(D[i, j], D[i, j - 1] + 1)

        # pass2
        for i in range(h - 1, -1, -1):
            for j in range(w - 1, -1, -1):
                if img[i, j] == 0:
                    D[i, j] = 0
                else:
                    if i < h - 1:
                        D[i, j] = min(D[i, j], D[i + 1, j] + 1)
                    if j < w - 1:
                        D[i, j] = min(D[i, j], D[i, j + 1] + 1)

        return D

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

class Skeleton:
    def zhang_algo(self, img):
        cleaned_skeleton = np.pad(
            img, pad_width=1, mode='constant', constant_values=0)
        rows, cols = cleaned_skeleton.shape
        skeleton = np.zeros((rows, cols), dtype=np.uint8)
        skeleton[:, :] = cleaned_skeleton > 0
        pixel_removed = True
        first_sub_iter = True
        while pixel_removed:
            pixel_removed = False
            # Sub-iterations
            # Iteration over the image
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    if (skeleton[i, j] == 1):  # avoid already zero pixels
                        neighbours = self.get_neighbours(i, j, skeleton)
                        P2, P3, P4, P5, P6, P7, P8, P9 = neighbours
                        B = sum(neighbours)
                        A = self.numberOfZeroOnePatterns(neighbours)
                        if (2 <= B <= 6 and A == 1):
                            m1 = P2 * P4 * P6 if first_sub_iter else P2 * P4 * P8
                            m2 = P4 * P6 * P8 if first_sub_iter else P2 * P6 * P8
                            if (m1 == 0 and m2 == 0):
                                cleaned_skeleton[i, j] = 0
                                pixel_removed = True
            skeleton[:, :] = cleaned_skeleton[:, :]
            first_sub_iter = not first_sub_iter
        return skeleton[1:-1, 1:-1]

    def get_neighbours(self,i, j, img):

        return [img[i - 1, j], img[i - 1, j + 1], img[i, j + 1], img[i + 1, j + 1],
                img[i + 1, j], img[i + 1, j - 1], img[i, j - 1], img[i - 1, j - 1]]

    def numberOfZeroOnePatterns(self,neighbours):
        n = neighbours + neighbours[0:1]  # P2, P3, ... , P8, P9, P2
        # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)
        return sum((a, b) == (0, 1) for a, b in zip(n, n[1:]))
