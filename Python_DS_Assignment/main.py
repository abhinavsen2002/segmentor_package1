import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage

from my_package.data.transforms import BlurImage, FlipImage, RotateImage, CropImage, RescaleImage
from my_package.analysis import plot_visualization

from my_package.data import Dataset
from my_package import model
from numpy import asarray

def main():
    path1 = "C:\\CS29006_SW_Lab_Spr2022-master\\Python_DS_Assignment\\data\\annotations.jsonl"
    tRotate = RotateImage(45)
    tBlur = BlurImage(2)
    tRotate2 = RotateImage(90)
    tUpscale = RescaleImage((1280, 852))
    tDownscale = RescaleImage((320, 213))
    tFlip = FlipImage('horizontal')
    d = Dataset(path1, [])

    path2 = 'C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment'
    for i in range(10):
        plot_visualization(d[i], path2+"/analysis1/OriginalImg"+str(i)+".png")

    d1 = Dataset(path1, [tFlip])
    d2 = Dataset(path1, [tBlur])
    d3 = Dataset(path1, [tUpscale])
    d4 = Dataset(path1, [tDownscale])
    d5 = Dataset(path1, [tRotate2])
    d6 = Dataset(path1, [tRotate])
    plot_visualization(d1[3], path2+"/analysis2/flipped.png")
    plot_visualization(d2[3], path2+"/analysis2/blurred.png")
    plot_visualization(d3[3], path2+"/analysis2/upscaled.png")
    plot_visualization(d4[3], path2+"/analysis2/downscaled.png")
    plot_visualization(d5[3], path2+"/analysis2/90Rotated.png")
    plot_visualization(d6[3], path2+"/analysis2/45Rotated.png")




if __name__ == '__main__':
    main()