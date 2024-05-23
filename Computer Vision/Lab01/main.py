from Lab01 import Lab01

fn1 = './data/Fig0107.tif'
fn2 = './data/lena.jpg'

task1 = [[176, 94, 201, 219],
         [37, 161, 16, 88],
         [71, 129, 177, 81],
         [41, 198, 107, 19]]

task2_1 = [[19, 171, 91, 68],
           [123, 99, 74, 195],
           [85, 71, 208, 18],
           [241, 212, 189, 68]]

task2_2 = [[106, 97, 190, 5],
           [81, 64, 183, 82],
           [71, 200, 251, 94],
           [181, 76, 9, 18]]

def main():
    w2 = week02()

    # task1
    #w2.task_flip(task1)
    #w2.task_flop(task1)
    #w2.task_flip_flop(task1)
    #w2.task_invert(task1)
    #w2.task_rotate90(task1)

    # task2
    #w2.task2_sum(task2_1, task2_2)
    #w2.task2_difference(task2_1, task2_2)
    #w2.task2_Absolute_Difference(task2_1, task2_2)

    #task3
    mode = 0
    img = w2.imRead(fn2, mode)
    #w2.imShow(img)
    #w2.Horizontal_flip(img)
    #w2.Vertical_flip(img)
    #w2.HV_flip(img)
    #w2.rotate(img, 90.0)
    #w2.rotate(img, 180.0)
    #w2.Resize(img, 500, 100)
    #w2.Contrast_enhancement(img)

    mode = 1
    img = w2.imRead(fn2, mode)
    #w2.Horizontal_flip(img)
    #w2.Vertical_flip(img)
    #w2.HV_flip(img)
    #w2.rotate(img, 90.0)
    #w2.rotate(img, 180.0)
    #w2.Resize(img, 80, 80)
    #w2.Resize(img, 500, 100)
    #w2.rgb_Contrast_enhancement(img)


if __name__ == '__main__':
    main()

