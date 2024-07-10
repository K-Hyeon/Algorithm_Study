from Lab04 import ConnectedComponents, utils, TemplateMatching, Skeleton
import cv2 as cv
import matplotlib.pyplot as plt

input1 = './data/coins.png'
input2 = './data/horse.png'
input3 = './data/fruits.png'
input4 = './data/image1.png'
input5 = './data/template1.png'
savepath = './data/bimg1.jpg'
flag = 0

def main():
    ut = utils()

    # task1
    # img1 = ut.imRead(input2, flag)
    # bimg = ut.binarize(img1, 126)

    # 1-1. The floodfill method of Algorithm 4.5.
    # 1-2. Implement the connected components method of Algorithm 4.7.
    # 1-3. Compute the region properties such as moments, area, perimeter, and centroid for each region obtained in step-2.
    # cc = ConnectedComponents(bimg)
    # components, lables = cc.getCC()
    """
    for r in lables: print(r)
    for c in components: print(c)
    """
    #cc.getProperties(components)
    #ut.imShow(lables)

    # task2
    tm = TemplateMatching()
    flag = 0

    print("image1: ", end='')
    img1 = ut.imRead(input4, flag)
    print("template1: ", end='')
    tem1 = ut.imRead(input5, flag)
    print()
    #btem = ut.binarize(tem1, 126)

    score, mloc, MM = tm.tempMatching(img1, tem1)
    print("score:", score)
    print("coordinate:", mloc)

    img = cv.imread(input4)
    tem = cv.imread(input5)
    tm.templatematchingCV(img, tem)

    # img = cv.imread('./data/image1.png')
    # x = 40 + mloc[1]//2
    # y = -25 - mloc[0]//2
    # width = 186 // 2
    # height = 252 // 2
    # # width = (tem1.shape[1])//2
    # # height = (tem1.shape[0])//2
    # cv.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2) # blue color
    # cv.imshow("Image with Rectangle", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # for r in MM:
    #     print(r)

    # result_image = tm.draw_rectangle(img1, tem1, mloc)
    #
    # # 이미지를 표시합니다.
    # cv.imshow('Result Image', result_image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # D = tm.ChamferDT(btem)

    # for r in D:
    #     print(r)
    # ut.imShow(D)

    # MR = tm.tmCV()
    # for r in MR:
    #     print(r)

    """
    # Skeleton
    sk = Skeleton()

    img1 = ut.imRead(input2, flag)
    bimg = ut.binarize(img1, 126)
    sk1 = sk.zhang_algo(bimg)
    ut.imShow(sk1)
    """

if __name__ == '__main__':
    main()
