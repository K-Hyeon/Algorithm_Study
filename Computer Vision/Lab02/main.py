from Lab02 import Utils, HistProc, Bsubtraction

input1 = './data/Fig0107.tif'
input2 = './data/lena.jpg'
input3 = './data/test1.jpg'
savepath = './data/savedImage.jpg'

flag = 0
task1 = [[5,8,3,7],
        [1,3,3,9],
        [6,8,2,7],
        [4,1,0,9]]
task1_href = [1, 1, 1, 0, 2, 2, 2, 0, 4, 3]

def main():
    # task1
    hp = HistProc()
    # 1-1. Histogram
    # 1-2. Normalized histogram (PDF)
    #hp.task1_plotHistPdf(task1)
    # 1-3. Cumulative normalized histogram (CDF)
    #hp.task1_plotCDF(task1)
    # 1-4. Histogram Equalization
    #hp.task1_plotEq(task1)
    # 1-5. Histogram Matching with given reference histogram href =  [1 1 1 0 2 2 2 0 4 3]
    #hp.task1_Match(task1, task1_href) # print href hist and href cdf
    # hp.task1_plotMatch(task1, task1_href)

    # task3
    B = Bsubtraction()
    ut = Utils()
    # 3-1. Reading a video
    B.vRead()
    # 3-2. Absolute Frame Difference(AFD)
    #B.frameDisff()
    # 3-3. Background Subtraction using(AFD)
    #getb = B.getB()
    #ut.imShow(getb)

if __name__ == '__main__':
    main()
