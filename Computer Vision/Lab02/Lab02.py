import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np


class HistProc:
    # task1
    def task1_plotHistPdf(self, arr):
        hist, pdf = self.task1_Hist_PDF(arr)
        x = np.linspace(0, 255, num=256)

        plt.figure(figsize=(15, 5))
        plt.subplot(1, 3, 1)
        plt.imshow(arr, cmap='gray')
        plt.title("Original Image")

        # 1-1. Histogram
        plt.subplot(1, 3, 2)
        plt.bar(x, hist)
        plt.title("1. Histogram")

        # 1-2. Normalized histogram (PDF)
        plt.subplot(1, 3, 3)
        plt.bar(x, pdf)
        plt.title("2. Normalized Histogram (PDF)")
        plt.show()

    def task1_plotCDF(self, arr):
        hist, pdf = self.task1_Hist_PDF(arr)
        cdf = self.task1_CDF(pdf)
        x = np.linspace(0, 255, num=256)

        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(arr, cmap='gray')
        plt.title("Original Image")

        # 1-3. Cumulative normalized histogram (CDF)
        plt.subplot(1, 2, 2)
        plt.bar(x, cdf)
        plt.title("3. Cumulative normalized histogram (CDF)")

        plt.show()

    def task1_plotEq(self, arr):
        EQ = self.task1_Eq(arr)
        x = np.linspace(0, 255, num=256)

        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(arr, cmap='gray')
        plt.title("Original Image")

        # 1-4. Histogram Equalization
        plt.subplot(1, 2, 2)
        plt.imshow(EQ, cmap='gray')
        plt.title("4. Histogram Equalization")

        plt.show()

    def task1_plotMatch(self, arr, href):
        Match = self.task1_Match(arr, href)

        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(arr, cmap='gray')
        plt.title("Original Image")

        # 1-5. Histogram Matching with given reference histogram href =  [1 1 1 0 2 2 2 0 4 3]
        plt.subplot(1, 2, 2)
        plt.imshow(Match, cmap='gray')
        plt.title("5. Histogram Matching with given reference histogram")

        plt.show()

    def task1_Hist_PDF(self, arr):
        hist = np.zeros([256], np.int32)
        if len(arr) < 6:
            for row in arr:
                for pixel in row:
                    hist[pixel] += 1
        else:
            for pixel in arr:
                hist[pixel] += 1

        pdf = [count / sum(hist) for count in hist]
        return hist, pdf

    def task1_CDF(self, pdf):
        cdf = np.zeros(256, float)
        cdf[0] = pdf[0]
        for i in range(1, 256):
            cdf[i] = cdf[i - 1] + pdf[i]
        return cdf

    def task1_Eq(self, arr):
        hist, pdf = self.task1_Hist_PDF(arr)
        cdf = self.task1_CDF(pdf)
        n = len(arr)

        cdf_t = np.round(cdf * 255, 0) # Rounded CDF values
        imgHE = np.zeros((n, n)) # Create a new image to store the value
        for i in range(0, n):
            for j in range(0, n):
                v = arr[i][j] # original value
                t = cdf_t[v] # t is new value
                imgHE[i][j] = t
        imgHE = np.uint8(imgHE)
        return imgHE

    def task1_Match(self, arr, href):
        n = len(arr)
        hist, pdf = self.task1_Hist_PDF(arr)
        hist_href, pdf_href = self.task1_Hist_PDF(href)

        cdf = self.task1_CDF(pdf)
        cdf_href = self.task1_CDF(pdf_href)

        inCDF = np.round(cdf * 255, 0)  # Rounded CDF values
        refCDF = np.round(cdf_href * 255, 0)

        T = self.task1_cdfT(inCDF, refCDF)
        imgHM = np.zeros((n, n)) # Create a new image to store the value
        for i in range(0, n):
            for j in range(0, n):
                v = arr[i][j]
                t = T[v]
                imgHM[i][j] = t
        imgHM = np.uint8(imgHM)


        x = np.linspace(0, 255, num=256)
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.bar(x, hist)
        plt.title("hist")

        plt.subplot(1, 2, 2)
        plt.bar(x, hist_href)
        plt.title("hist_href")
        plt.show()

        """"
        x = np.linspace(0, 255, num=256)
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.bar(x, cdf)
        plt.title("cdf")

        plt.subplot(1, 2, 2)
        plt.bar(x, cdf_href)
        plt.title("cdf_href")
        plt.show()
        """
        return imgHM


    def task1_cdfT(self, inCDF, refCDF):
        T = np.zeros(256)
        lcdf = len(inCDF)
        found = 0
        for s in range(lcdf):  # input
            for ref in range(lcdf):
                if refCDF[ref] >= inCDF[s]:
                    found = ref
                    break
            T[s] = found
        return T

    # writing a lecture
    """
    def imHistEq(self, img):
        ut = Utils()
        h, w = img.shape
        hist, pdf = self.imHist(img)
        cdf = self.cdfHist(pdf)

        cdf_t = np.round(cdf * 255, 0)
        imgHE = np.zeros((h, w))
        for i in range(0, h):
            for j in range(0, w):
                v = img[i, j] # original value
                t = cdf_t[v] # t is new value
                imgHE[i, j] = t
        imgHE = np.uint8(imgHE)
        ut.compareIms(img, imgHE)
        self.plotHist(img)
        self.plotHist(imgHE)
        self.plotcdf((imgHE))
        return imgHE

    def cdfHist(self, pdf):
        cdf = np.zeros(256, float)
        cdf[0] = pdf[0]
        for i in range(1, 256):
            cdf[i] = cdf[i - 1] + pdf[i]
        return cdf

    def plotcdf(self, img):
        hist, pdf = self.imHist(img)
        cdf = self.cdfHist(pdf)
        x = np.linspace(0, 255, num=256)
        plt.bar(x, cdf)
        plt.title('Gray Level Histogram')
        plt.xlabel("Gray values")
        plt.ylabel("Frequency")
        plt.show()

    def plotHist(self, img):
        hist, pdf = self.imHist(img)
        cdf = self.cdfHist(pdf)
        x = np.linspace(0, 255, num=256)
        plt.bar(x, pdf)
        # plt.bar(x, cdf)
        plt.title('Gray Level Histogram')
        plt.xlabel("Gray values")
        plt.ylabel("Frequency")
        plt.show()

    def imHist(self, img):
        h, w = img.shape
        hist = np.zeros([256], np.int32)
        for i in range(0, h):
            for j in range(0, w):
                hist[img[i, j]] += 1
        pdf = hist / (h * w)
        return hist, pdf

    def imHistMatch(self, img, timg):
        ut = Utils()
        h, w = img.shape
        h1, pdf1 = self.imHist(img)
        h2, pdf2 = self.imHist(timg)
        cdf1 = self.cdfHist(pdf1)
        cdf2 = self.cdfHist(pdf2)
        inCDF = np.round(cdf1 * 255, 0)
        refCDF = np.round(cdf2 * 255, 0)

        T = self.cdfT(inCDF, refCDF)
        imgHM = np.zeros((h, w))  # creating img
        for i in range(0, h):
            for j in range(0, w):
                v = img[i, j]
                t = T[v]  # 특정값 new value
                imgHM[i, j] = t
        imgHM = np.uint8(imgHM)

        plt.figure()
        plt.subplot(131)
        plt.imshow(img, cmap='gray')
        plt.subplot(132)
        plt.imshow(timg, cmap='gray')
        plt.subplot(133)
        plt.imshow(imgHM, cmap='gray')
        plt.show()

    def cdfT(self, inCDF, refCDF):
        T = np.zeros(256)
        lcdf = len(inCDF)
        found = 0
        for s in range(lcdf):  # input
            for ref in range(lcdf):
                if refCDF[ref] >= inCDF[s]:
                    found = ref
                    break
            T[s] = found
        return T
    """

class Bsubtraction:
    # Calculate the frame difference between the current frame and the previous frame.
    def frameDisff(self):
        vid = cv.VideoCapture('./data/vtest.avi')

        # Make sure the video is open
        if vid.isOpened() == False:
            print("Error in opening video...")

        ret, cframe = vid.read() # First frame
        pframe = cframe
        count = 1
        while(vid.isOpened()):
            cgray = np.array(cv.cvtColor(cframe, cv.COLOR_RGB2GRAY), dtype=float)
            pgray = np.array(cv.cvtColor(pframe, cv.COLOR_RGB2GRAY), dtype=float)

            fdiff = cv.absdiff(cgray, pgray) # Absolute frame difference
            fdiff = np.uint8(fdiff)

            cv.imshow("cFrame", cframe)
            cv.imshow("Differnece", fdiff)

            pframe = cframe.copy()
            ret, cframe = vid.read()

            # If the frame is not read properly, the loop is terminated.
            if ret != True:
                break

        vid.release()
        cv.waitKey(0)
        cv.destroyAllWindows()

    def getB(self):
        vid = cv.VideoCapture('./data/vtest.avi')

        # Make sure the video is open
        if vid.isOpened() == False:
            print("Error in opening video...")

        ret, frame1 = vid.read() # First frame
        B1 = np.array(cv.cvtColor(frame1, cv.COLOR_RGB2GRAY), dtype=float) # background img
        count = 1
        while(vid.isOpened()):
            ret, frame = vid.read() # Next frame
            if ret != True:
                break
            temp = np.array(cv.cvtColor(frame, cv.COLOR_RGB2GRAY), dtype=float) # new img
            B1 = np.add(B1, temp)
            count += 1
        vid.release()
        B = np.uint8(np.divide(B1, count))
        return B

    def vRead(self):
        vid = cv.VideoCapture('./data/vtest.avi')
        if vid.isOpened() == False:
            print("Error in opening video.")
        count = 0
        while(vid.isOpened()):
            count += 1
            ret, frame = vid.read()
            if ret == True:
                cv.imshow("Frame", frame)
                if cv.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        print("Number of frames = {}".format(count))
        vid.release()
        cv.destroyAllWindows()


class Utils:
    def imRead(self, fname, mode):
        img = cv.imread(fname, mode)
        if img is None:
            sys.exit("Could not read the image.")
        print(img.shape)
        return img

    def imWrite(self, img):
        filename = 'savedImage.jpg'
        img1 = cv.imread(img)
        if img1 is None:
            sys.exit("Could not read the image.")

        cv.imwrite(filename, img1)

    def imShow(self, img):
        if img is None:
            sys.exit("Not a valid image object")

        if len(img.shape)==2:
            plt.imshow(img, cmap = 'gray')
        else:
            plt.imshow(img)
        plt.show()

    def compareIms(self, img1, transformed, t1 = "Orignal1", t2 = "Orignal2",):
        fig = plt.figure()
        a1 = fig.add_subplot(1, 2, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(1, 2, 2)
        a2.imshow(transformed, cmap='gray')
        a2.set_title(t2)

        fig.tight_layout()
        plt.show()