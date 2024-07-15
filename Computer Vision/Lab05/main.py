from Lab05 import utils, Convolution, Kernels, LinearFiltering
import numpy as np
import matplotlib.pyplot as plt

input1 = './data/coins.png'
input2 = './data/horse.png'
input3 = './data/fruits.png'
input4 = './data/image1.png'
input5 = './data/template1.png'
savepath = './data/bimg1.jpg'
flag = 0

# Task1
task1_img = np.array([[5, 4, 0, 3],
                      [6, 2, 1, 8],
                      [7, 9, 4, 2]])
task1_g = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

# Task2
task2_img = np.array([[218, 87, 246, 64, 175],
                      [106, 161, 231, 32, 207],
                      [16, 141, 136, 140, 202],
                      [86, 253, 55, 112, 188],
                      [73, 85, 165, 209, 99]])
def main():
    # Task1
    ut = utils()
    # ut.compareImgs(task1_img, task1_g)
    con = Convolution()
    # output = con.conv2D(task1_img, task1_g)
    # print("img: ", task1_img)
    # print("kernel: ", task1_g)
    # print("result: ", output)
    # ut.compareImgs(task1_img, output)

    # Task2
    lf = LinearFiltering()
    # output = lf.integral_image(task2_img)
    # print(output)
    # ut.compareImgs(task2_img, output)

    # Task3
    kr = Kernels()
    img = ut.imRead(input1, flag)
    conv = con.conv2D(img, kr.box_kernel(3))
    # ut.compareImgs(img, conv)


    #task4
    kr = Kernels()
    img = ut.imRead(input1, flag)

    gx = con.conv2D(img, kr.Sobelx)
    gy = con.conv2D(img, kr.Sobely)
    mag = np.abs(gx) + np.abs(gy)
    # ut.compareImgs(gx, gy, t1='Smoothed Image X', t2='Smoothed Image Y')  # Smoothed Image
    # ut.compareImgs(img, mag, "Original", t2='Gradient Magnitude')  # Gradient Magnitude
    #
    # out1 = con.conv2D(img, kr.gauss2D(7, 1))
    # out2 = con.conv2D(img, kr.gauss2D(7, 4))
    # difference = out2 - out1
    # ut.compareImgs(img, difference, t2='Difference of Gaussian(DOG)')  # Difference of Gaussian(DOG)
    # ut.compareImgs(img, np.abs(difference), t2='Gradient Magnitude')  # Gradient Magnitude


    # Lecture Code
    con = Convolution()
    #con.test_conv1d()
    #con.test_conv2d()

    kr = Kernels()
    # print(kr.box_kernel(3))
    # print(kr.box_kernel(5))
    # print(kr.box_kernel(7))

    ut = utils()
    img = ut.imRead(input1, flag)
    #oimg = con.conv2D(img, kr.box_kernel(11)) #output Image
    #ut.compareImgs(img, oimg)
    # print(kr.gauss2D(3, 1))
    """
    k1 = np.array([1,1,1]) * (1/3)
    k2 = np.array([1,1,1]) * (1/3)
    oimg1 = con.conv2D(img, kr.gauss2D(3, 1))
    oimg2 = con.conv2D(oimg1, kr.gauss2D(3, 1))
    oimg = con.conv2D(img, kr.gauss2D(3, 1))
    ut.compareImgs(img, oimg)

    k1 = np.array([1, 1, 1]) * (1 / 3)
    k2 = np.transpose(k1)
    oimg1 = con.conv1D(img, k1)
    oimg2 = con.conv1D(oimg1, k2)
    ut.compareImgs(oimg1, oimg2)
    """

    #print(kr.box_kernel_x(3))
    #print(kr.box_kernel_y(3))
    # img = ut.imRead(input1, flag)
    # img1 = np.array([1, 1, 1]) / 3
    # oimg = np.array([1, 1, 1]) / 3
    # for i in range(20):
    #     oimg = con.conv1D(oimg, img1)
    #     plt.plot(oimg)
    #     plt.show()

    #oimg1 = con.conv2D(img, kr.box_kernel_x(5))
    #oimg2 = con.conv2D(oimg1, kr.box_kernel_y(5))
    #ut.compareImgs(oimg1, oimg2)

    # lf = LinearFiltering()
    # img = ut.imRead(input1, flag)
    # oimg = lf.box_filter2(img, 25)
    # ut.compareImgs(img, oimg)

    img = ut.imRead(input4, flag)
    # gx = con.conv2D(img, kr.Prewittx)
    # gy = con.conv2D(img, kr.Prewitty)
    gx = con.conv2D(img, kr.Sobelx)
    gy = con.conv2D(img, kr.Sobelx)
    mag = np.abs(gx) + np.abs(gy)
    # ut.compareImgs(gx, gy)
    # ut.compareImgs(img, mag)
    # lout = con.conv2D(img, kr.L0)
    # ut.compareImgs(img, lout)
    # ut.compareImgs(img, np.abs(lout))

    #out1 = con.conv2D(img, kr.box_kernel(3))
    # out2 = con.conv2D(img, kr.box_kernel(7))
    # out1 = con.conv2D(img, kr.gauss2D(5, 1))
    # out2 = con.conv2D(img, kr.gauss2D(5, 3))
    # out3 = out1 - out2
    # ut.compareImgs(img, out3)
    # ut.compareImgs(img, np.abs(out3))


if __name__ == '__main__':
    main()


