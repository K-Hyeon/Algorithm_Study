import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys

class binary_image:
    # task1
    def SetToBinary(self, B):
        # Check the size of the array.
        B_list = sorted(B, reverse=True)
        max_x, max_y = 0, 0
        for x, y in B_list:
            max_x = max(max_x, x)
            max_y = max(max_y, x)

        # Create Array.
        Bimg = np.zeros((max_x+1, max_y+1))
        for x, y in B_list:
            Bimg[x][y] = 1
        return Bimg.tolist()

    # A ∪ B ≡ {z : z ∈ A or z ∈ B}
    def union(self, arr1, arr2):
        n = len(arr1)
        unoin_img = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if (arr1[i][j] == 1) or (arr2[i][j] == 1):
                    unoin_img[i][j] = 1
        return unoin_img

    # A ∩ B ≡ {z : z ∈ A and z ∈ B}
    def intersection(self, arr1, arr2):
        h, w = len(arr1), len(arr1[0])
        inter_img = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                if arr1[i][j] == arr2[i][j]:
                    inter_img[i][j] = arr1[i][j]
        return inter_img

    # A_b ≡ {z : z = a + b, a ∈ A}
    def translation(self, arr1, b):
        h, w = len(arr1), len(arr1[0])
        trans_img = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                ni = i + b[0]
                nj = j + b[1]

                # 범위 초과
                if (ni < 0) or (ni >= w) or (nj < 0) or (nj >= h):
                    continue

                trans_img[ni][nj] = arr1[i][j]
        return trans_img

    # reflection = {z : z = −b, b ∈ B}
    def reflection(self, arr):
        n = len(arr)
        reflec_img = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                reflec_img[n-1-i][n-1-j] = arr[i][j]
        return reflec_img

    # complement =  {z : z ∈ A}
    def Complement(self, arr):
        h, w = len(arr), len(arr[0])
        complement_img = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:
                    complement_img[i][j] = 0
                else:
                    complement_img[i][j] = 1
        return complement_img

    # A ⧹ A =  {z : z ∈ A, z ∈ B}
    def difference(self, arr1, arr2):
        intersection = self.intersection(arr1, arr2)

        n = len(arr1)
        difference_img = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                difference_img[i][j] = arr1[i][j] - intersection[i][j]
        return difference_img

    # task2
    def BinaryToSet(self, arr):
        n = len(arr)
        Set = set()
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 1:
                    Set.add((i, j))
        return Set

    def Set_Minkowski(self, arr):
        h, w = len(arr), len(arr[0])
        Set = set()
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:
                    Set.add((i -2, j - 2))
        return Set

    def minkowski_addition(self, arr1, arr2):
        set_a = self.Set_Minkowski(arr1)
        set_b = self.Set_Minkowski(arr2)

        n = len(arr1)
        center = n//2
        addition = np.zeros((n, n))
        for a in set_a:
            for b in set_b:
                nx = a[0] + b[0]
                ny = a[1] + b[1]
                if (nx >= -center) and (nx <= center) and (ny >= -center) and (ny <= center):
                    addition[a[0]+b[0]+2][a[1]+b[1]+2] = 1
        return addition

    def minkowski_subtraction(self, arr1, arr2):
        #set_a = self.Set_Minkowski(arr1)
        set_b = self.Set_Minkowski(arr2)
        list_b = list(set_b)

        result = self.translation(arr1, list_b[0])
        for b in list_b[1:]:
            move = self.translation(arr1, b)
            result = self.intersection(move, result)

        return result

    # task3
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
    def makeSE(self, t='cross3'):
        if t == 'cross3':
            return np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype='int')

        if t == 'cross5':
            return np.array([[0, 0, 1, 0, 0],
                             [0, 1, 1, 1, 0],
                             [1, 1, 1, 1, 1],
                             [0, 1, 1, 1, 0],
                             [0, 0, 1, 0, 0]], dtype='int')

        if t == 'box3':
            return np.array([[0, 1, 1], [0, 1, 1], [0, 1, 1]], dtype='int')

        if t == 'box5':
            return np.array([[1, 1, 1, 1, 1],
                             [1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 1],
                             [1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 1]], dtype='int')

        # return np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype='int')
        return np.ones((5, 5), dtype='int')

    def padd_img(self, img, psize):
        h, w = img.shape
        pimg = np.zeros((h + 2 * psize, w + 2 * psize))
        pimg[psize:-psize, psize:-psize] = img
        return pimg

    def imDilate(self, img, SE):
        h, w = img.shape
        s1, s2 = SE.shape
        psize = s1 // 2
        pimg = self.padd_img(img, psize)
        dimg = np.zeros(pimg.shape)
        for i in range(h):
            for j in range(w):
                if pimg[i, j] == 1:
                    for m in range(s1):
                        for n in range(s2):
                            if SE[m, n] == 1:
                                dimg[i + m, j + n] = 1
        return dimg[:h, :w]

    def imErode(self, img, SE):
        h, w = img.shape
        s1, s2 = SE.shape
        psize = s1 // 2
        pimg = self.padd_img(img, psize)
        eimg = np.zeros(pimg.shape)
        for i in range(h):
            for j in range(w):
                if pimg[i, j] == 0:
                    for m in range(s1):
                        for n in range(s2):
                            if SE[m, n] == 0:
                                eimg[i+m, j+n] = 1
        return eimg[:h, :w]

    def imOpen(self, img, SE):
        eimg = self.imErode(img, SE)
        oimg = self.imDilate(eimg, SE)
        return oimg

    def imClose(self, img, SE):
        dimg = self.imDilate(img, SE)
        cimg = self.imErode(dimg, SE)
        return cimg

    def imAnd(self, img1, img2):  # 합집합
        h, w = img1.shape
        aimg = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                if img1[i, j] == img2[i, j]:
                    aimg[i, j] = 1
        return aimg

    def hitMiss(self, img, SE):
        h, w = img.shape
        s1, s2 = SE.shape
        SE_hit = np.zeros((s1, s2))
        SE_miss = np.zeros((s1, s2))
        for i in range(s1):
            for j in range(s2):
                if SE[i, j] == 1:
                    SE_hit[i, j] = 1
                if SE[i, j] == -1:
                    SE_miss[i, j] = 1
        ehit = self.imErode(img, SE_hit)
        cimg = self.Complement(img)
        emiss = self.imErode(cimg, SE_miss)
        hmimg = self.imAnd(ehit, emiss)
        # print(ehit.shape)
        # print(emiss.shape)
        return hmimg

    def imErode_arr(self, img, SE):
        s1, s2 = SE.shape
        psize = s1 // 2
        pimg = self.padd_img(img, psize) # Padding is filled with zero.
        h, w = pimg.shape
        eimg = np.zeros(pimg.shape)
        for i in range(h):
            for j in range(w):
                # if you don't exceed the range
                if (i+len(SE) < h) and (j+len(SE) < w):
                    match = True
                    for m in range(s1):
                        for n in range(s2):
                            if (SE[m][n] == 1) and (pimg[i + m, j + n] == 0):
                                #print(i+m, j+n, m, n, SE[m][n], pimg[i + m, j + n])
                                match = False
                                break
                        if match == False: break
                    if match == True:
                        eimg[i + psize, j + psize] = 1

        return eimg[psize:-psize,psize:-psize]

    def imAnd_arr(self, img1, img2):
        h, w = img1.shape
        aimg = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                if img1[i, j] == img2[i, j]:
                    if img1[i, j] == 1:
                        aimg[i, j] = 1
                    else:
                        aimg[i, j] = 0

        return aimg

    # A ⊛ B = (A⊖ˇBON ) ∩ (A⊖ˇBOFF )
    def hitMiss_arr(self, img, SE):
        h, w = img.shape
        s1, s2 = SE.shape
        SE_hit = np.zeros((s1, s2))
        SE_miss = np.zeros((s1, s2))
        for i in range(s1):
            for j in range(s2):
                if SE[i, j] == 1:
                    SE_hit[i, j] = 1
                if SE[i, j] == 0:
                    SE_miss[i, j] = 1
        # ehit = self.
        ehit = self.imErode_arr(img, SE_hit)  # A⊖ˇBON
        cimg = self.Complement(img)  # ⌝A
        emiss = self.imErode_arr(cimg, SE_miss)  # (A⊖ˇBOFF )
        hmimg = self.imAnd_arr(ehit, emiss)  # (A⊖ˇBON ) ∩ (A⊖ˇBOFF )

        return hmimg

    # lecture code
    """       
    def complement(self, img):
        return abs(np.array(img, copy=True) - 1)

    def sub(self, img1, img2):
        h, w = img1.shape
        simg = np.array(img1, copy=True)
        for i in range(h):
            for j in range(w):
                if img1[i, j] == img2[i, j]:
                    simg[i, j] = 0
        return simg
    """

    # task4
    def task4_And(self, img1, img2):
        h, w = img1.shape
        aimg = np.zeros((h, w))
        for i in range(h):
            for j in range(w):
                if img1[i, j] == img2[i, j]:
                    if img1[i, j] == 1:
                        aimg[i, j] = 1
                    else:
                        aimg[i, j] = 0

        return aimg

    # I ⊟ B ≡ I∩⌝ (I ⊛ B)
    def thinning(self, arr, SE):
        s1, s2 = SE.shape
        psize = s1 // 2
        pimg = self.padd_img(arr, psize)  # Padding is filled with zero.
        process_img = self.padd_img(arr, psize)
        eimg = self.padd_img(arr, psize)
        h, w = pimg.shape
        for i in range(h):
            for j in range(w):
                # if you don't exceed the range
                if (i + len(SE) < h) and (j + len(SE) < w):
                    match = True
                    for m in range(s1):
                        for n in range(s2):
                            if ((SE[m][n] == 1) and (pimg[i + m, j + n] == 0)) or (
                                    (SE[m][n] == 0) and (pimg[i + m, j + n] == 1)):
                                match = False
                                break

                        if match == False: break
                    if match == True:
                        process_img[i + psize, j + psize] = 0.5
                        eimg[i + psize, j + psize] = 0
                if eimg[i][j] == 0.5:
                    eimg[i][j] = 0

        return process_img[psize:-psize, psize:-psize], eimg[psize:-psize, psize:-psize]



class utils:
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

    def compareImgs2(self, img1, img2, img3, t1="Image1", t2="Image2", t3="Transformed Image"):
        # plot
        fig = plt.figure()

        a1 = fig.add_subplot(1, 3, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(1, 3, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        a3 = fig.add_subplot(1, 3, 3)
        a3.imshow(img3, cmap='gray')
        a3.set_title(t3)

        fig.tight_layout()
        plt.show()

    def compareImgs8(self, img1, img2, img3, img4, img5, img6, img7, img8, t1="Image1", t2="Image2", t3="Image3", t4="Image4", t5="Image5", t6="Image6", t7="Image7", t8="Transformed Image"):
        # plot
        fig = plt.figure()

        a1 = fig.add_subplot(3, 3, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(3, 3, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        a3 = fig.add_subplot(3, 3, 3)
        a3.imshow(img3, cmap='gray')
        a3.set_title(t3)

        a4 = fig.add_subplot(3, 3, 4)
        a4.imshow(img4, cmap='gray')
        a4.set_title(t4)

        a5 = fig.add_subplot(3, 3, 5)
        a5.imshow(img5, cmap='gray')
        a5.set_title(t5)

        a6 = fig.add_subplot(3, 3, 6)
        a6.imshow(img6, cmap='gray')
        a6.set_title(t6)

        a7 = fig.add_subplot(3, 3, 7)
        a7.imshow(img7, cmap='gray')
        a7.set_title(t7)

        a8 = fig.add_subplot(3, 3, 8)
        a8.imshow(img8, cmap='gray')
        a8.set_title(t8)

        fig.tight_layout()
        plt.show()

    def compareImgs9(self, img1, img2, img3, img4, img5, img6, img7, img8, img9, t1="Image1", t2="Image2", t3="Image3", t4="Image4", t5="Image5", t6="Image6", t7="Image7", t8="Image8", t9="Transformed Image"):
        # plot
        fig = plt.figure()

        a1 = fig.add_subplot(3, 3, 1)
        a1.imshow(img1, cmap='gray')
        a1.set_title(t1)

        a2 = fig.add_subplot(3, 3, 2)
        a2.imshow(img2, cmap='gray')
        a2.set_title(t2)

        a3 = fig.add_subplot(3, 3, 3)
        a3.imshow(img3, cmap='gray')
        a3.set_title(t3)

        a4 = fig.add_subplot(3, 3, 4)
        a4.imshow(img4, cmap='gray')
        a4.set_title(t4)

        a5 = fig.add_subplot(3, 3, 5)
        a5.imshow(img5, cmap='gray')
        a5.set_title(t5)

        a6 = fig.add_subplot(3, 3, 6)
        a6.imshow(img6, cmap='gray')
        a6.set_title(t6)

        a7 = fig.add_subplot(3, 3, 7)
        a7.imshow(img7, cmap='gray')
        a7.set_title(t7)

        a8 = fig.add_subplot(3, 3, 8)
        a8.imshow(img8, cmap='gray')
        a8.set_title(t8)

        a9 = fig.add_subplot(3, 3, 9)
        a9.imshow(img9, cmap='gray')
        a9.set_title(t9)

        fig.tight_layout()
        plt.show()
