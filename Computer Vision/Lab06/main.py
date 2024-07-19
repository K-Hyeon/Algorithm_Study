from Lab06 import utils, noisy_image, nan_linear_filtering, measure

input1 = './data/cameraman.tif'
input2 = './data/clutter1.bmp'
input3 = './data/foggysf1.jpg'
input4 = './data/foggysf2.jpg'
input5 = './data/toysflash.png'
input6 = './data/toysnoflash.png'
savepath = './data/bimg1.jpg'
flag = 0

def main():
    ut = utils()
    no = noisy_image()
    nlf = nan_linear_filtering()
    ms = measure()
    img = ut.imRead(input1, flag)

    # Task1
    nimg1 = no.Gaussian_noise(img, 0.1, 0.2)
    nimg2 = no.salt_pepper_noise(img, 0.1, 0.2)

    # Task2
    # 2.1. Median Filter
    # MFilter = nlf.median_filter(nimg2, 3)
    # ut.compareImgs(nimg2, MFilter, t1='Salt Pepper Noise', t2='Median Filter')
    # print('MSE = {:.2f}, PSNR = {:.2f}'.format(ms.MSE(img, MFilter), ms.PSNR(img, MFilter)))

    # MFilter2 = nlf.median_filter(nimg1, 3)
    # ut.compareImgs(nimg1, MFilter2, t1='Gaussian Noise', t2='Median Filter')

    # 2.2. Diffusion Filter
    # DFilter = nlf.anisotropic_diffusion(nimg2, 5, 5, 5)
    # ut.compareImgs(nimg2, DFilter, t1='Salt Pepper Noise', t2='Diffusion Filter')

    # DFilter2 = nlf.anisotropic_diffusion(nimg1, 5, 5, 5)
    # ut.compareImgs(nimg1, DFilter2, t1='Gaussian Noise', t2='Diffusion Filter')

    # 2.3. Non-local mean filter
    # NLM = nlf.non_local_mean(nimg1, 3, 3, 15)
    # ut.compareImgs(nimg1, NLM, t1='Salt Pepper Noise', t2='Non Local Mean')

    # NLM2 = nlf.non_local_mean(nimg2, 3, 3, 15)
    # ut.compareImgs(nimg2, NLM2, t1='Gaussian Noise', t2='Non Local Mean')

    # 2.4. Bilateral filter
    # BFilter = nlf.bilateral_filter(nimg1, 3, 3, 15)
    # ut.compareImgs(nimg1, BFilter, t1='Salt Pepper Noise', t2='Bilateral filter')

    # BFilter2 = nlf.bilateral_filter(nimg2, 3, 3, 15)
    # ut.compareImgs(nimg2, BFilter2, t1='Gaussian Noise', t2='Bilateral filter')

    # 2.5. Mean-shift filter
    # MSFilter = nlf.mean_shift_filter(nimg1, 3, 3, 15)
    # ut.compareImgs(nimg1, MSFilter, t1='Salt Pepper Noise', t2='Mean-shift filter')

    # MSFilter2 = nlf.mean_shift_filter(nimg2, 3, 15, 15)
    # ut.compareImgs(nimg2, MSFilter2, t1='Gaussian Noise', t2='Mean-shift filter')


if __name__ == '__main__':
    main()
