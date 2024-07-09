from Lab03 import binary_image, utils
import numpy as np

input1 = './data/coins.png'
input2 = './data/spoons.png'
input3 = './data/fruits.png'

# task1
A = [[1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0]]
B = {(1,1), (2,1), (1,2), (2,2), (3,2), (1,3), (3,3)}
b = (1,1)

# task2
task2_A1 = np.array([[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0],
                     [0, 0, 1, 1, 0],
                     [0, 0, 0, 0, 0]])
task2_A2 = np.array([[0, 1, 1, 0, 0],
                     [0, 1, 1, 1, 0],
                     [1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 0],
                     [0, 0, 1, 0, 0]])
task2_B = np.array([[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0]])

test1 = np.array([[0, 0, 1, 0, 0],
                     [0, 1, 1, 1, 0],
                     [1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 0],
                     [0, 0, 1, 0, 0]])
test2 = np.array([[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0]])

# task3
task3_test1 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

# task4
task4_img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
task4_test1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

flag = 0

def main():
    # task1
    ut = utils()
    bi = binary_image()
    # 1-1. Binary Image
    Binary_B = bi.SetToBinary(B)
    #ut.compareImgs(A, Binary_B, t1='A', t2='B')
    # 1-2. union (A ∪ B)
    #ut.compareImgs2(A, Binary_B, bi.union(A, Binary_B), t1='A', t2='B', t3='Union Image (A ∪ B)')
    # 1-3. intersection (A ∩ B)
    #ut.compareImgs2(A, Binary_B, bi.intersection(A, Binary_B), t1='A', t2='B', t3='Intersection Image (A ∩ B)')
    # 1-4. translation (A_b)
    #ut.compareImgs(A, bi.translation(A, b), t1='A, b = (1,1)', t2='Translation Image')
    # 1-5. reflection
    #ut.compareImgs(Binary_B, bi.reflection(Binary_B), t1='A, b = (1,1)', t2='Reflection Image')
    # 1-6. complement
    #ut.compareImgs(A, bi.Complement(A), t1='A', t2='Complement Image')
    # 1-7. difference (A ⧹ B)
    #ut.compareImgs2(A, Binary_B, bi.difference(A, Binary_B), t1='A', t2='B', t3='difference Image')

    # task2
    # 2-1. Minkowski addition for sets A1 and B
    #ut.compareImgs2(task2_A1, task2_B, bi.minkowski_addition(task2_A1, task2_B), t1='A1', t2='B', t3='Minkowski addition')
    # 2-2. Minkowski subtraction for sets A2 and B
    #ut.compareImgs2(task2_A2, task2_B, bi.minkowski_subtraction(task2_A2, task2_B), t1='A2', t2='B', t3='Minkowski subtraction')
    #ut.compareImgs2(test1, test2, bi.minkowski_subtraction(test1, test2), t1='test1', t2='test2', t3='Minkowski subtraction')

    #task3
    img1 = ut.imRead(input1, flag)
    #ut.imShow(img1) # original image
    # 3-1. Dilate
    bimg = bi.binarize(img1)
    SE = bi.makeSE('cross5')
    #ut.compareImgs(img1, bi.imDilate(bimg, SE), t2='Dilated(cross5)')
    # 3-2. Erode
    SE = bi.makeSE('cross5')
    #ut.compareImgs(img1, bi.imErode(bimg, SE), t2='Erode(cross5)')
    # 3-3. Open
    #ut.compareImgs(img1, bi.imOpen(bimg, SE), t2='Opened(cross5)')
    # 3-4. Close
    #ut.compareImgs(img1, bi.imClose(bimg, SE), t2='Closed(cross5)')
    # 3-5. Hit and Miss
    SE2 = np.array([[1,0,-1],[1,1,-1],[-1,0,-1]])
    #ut.compareImgs(img1, bi.hitMiss(bimg, SE), t2='Hit and Miss')
    # Test as an example of PPT
    SE = np.array([[-1, 0, 0, 0, -1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [-1, 0, 0, 0, -1]])
    #ut.compareImgs(task3_test1, bi.hitMiss_arr(task3_test1, SE), t2='Hit and Miss')

    # task4
    # task4-1. Apply all 8 SEs as a sequence until convergence.
    task4_EdgeSEs = np.array([[0, 0, 0], [-1, 1, -1], [1, 1, 1]])
    #ut.compareImgs(task4_img, bi.thinning(task4_img, task4_EdgeSEs), t1='Original', t2='thinning')
    # Test as an example of PPT
    Edge_SE1 = np.array([[0, 0, 0],[-1, 1, -1], [1, 1, 1]])
    Edge_SE2 = np.array([[1, -1, 0],[1, 1, 0], [1, -1, 0]])
    Edge_SE3 = np.array([[1, 1, 1],[-1, 1, -1], [0, 0, 0]])
    Edge_SE4 = np.array([[0, -1, 1],[0, 1, 1], [0, -1, 1]])

    Corner_SE1 = np.array([[-1, 0, 0], [1, 1, 0], [-1, 1, -1]])
    Corner_SE2 =np.array([[-1, 1, -1], [1, 1, 0], [-1, 0, 0]])
    Corner_SE3 = np.array([[-1, 1, -1], [0, 1, 1], [0, 0, -1]])
    Corner_SE4 = np.array([[0, 0, -1], [0, 1, 1], [-1, 1, -1]])

    process1, process11 = bi.thinning(task4_img, Edge_SE1)
    process2, process22 = bi.thinning(process11, Edge_SE3)
    process3, process33 = bi.thinning(process22, Edge_SE1)
    process4, process44 = bi.thinning(process33, Edge_SE3)
    process5, process55 = bi.thinning(process44, Corner_SE1)
    process6, process66 = bi.thinning(process55, Corner_SE2)
    process7, process77 = bi.thinning(process66, Corner_SE4)
    #ut.compareImgs9(task4_img, process1, process2, process3, process4, process5, process6, process7, process77, t1 = 'Original', t2 = 'process1', t3 = 'process2', t4 = 'process3', t5 = 'process4', t6 = 'process5', t7 = 'process6', t8 = 'process7', t9='Result')

    # task4-2. Apply the 4 edge SEs as a set until convergence, then apply the 4 corner SEs until convergence.
    process1, process11 = bi.thinning(task4_img, Edge_SE1)
    process2, process22 = bi.thinning(process1, Edge_SE2)
    process3, process33 = bi.thinning(process2, Edge_SE3)
    process4, process44 = bi.thinning(process3, Edge_SE4)

    process5, process55 = bi.thinning(process44, Edge_SE1)
    process6, process66 = bi.thinning(process5, Edge_SE2)
    process7, process77 = bi.thinning(process6, Edge_SE3)
    process8, process88 = bi.thinning(process7, Edge_SE4)

    process9, process99 = bi.thinning(process88, Corner_SE1)
    process10, process1010 = bi.thinning(process99, Corner_SE2)
    process11, process1111 = bi.thinning(process1010, Corner_SE3)
    process12, process1212 = bi.thinning(process1111, Corner_SE4)
    result = process1212
    ut.compareImgs8(task4_img, process4, process8, process9, process10, process11, process12, result, t1='Original', t2='process1', t3='process2', t4='process3', t5='process4', t6='process5', t7='process6', t8='Result')


if __name__ == '__main__':
    main()


