import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import random

def menu():
    print("****************** WELCOME TO THE PROGRAM ******************\n")
    print("[1] Read the input image\n")
    print("[2] Convert the image into gray-scale\n")
    print("[3] Show the histogram of the image\n")
    print("[4] Modify the brightness of the image using gamma correction\n    with arandom gamma value using look-up table\n")
    print("[5] Modify the brightness of the image using gamma correction\n    with arandom gamma value by modifying each pixel individually\n")
    print("[0] Exit the program.")

def Histogram(before,after):
    # histogram for the original image
    histo = cv.calcHist([before], [0], None, [256], [0, 256])
    # histogram for the output image
    histo_output = cv.calcHist([after], [0], None, [256], [0, 256])
    plt.figure()
    plt.xlabel("Intensity")
    plt.ylabel("% of pixels")
    plt.xlim([0, 256])
    plt.locator_params(axis='x', nbins=50)
    plt.locator_params(axis='y', nbins=20)
    plt.plot(histo)
    plt.plot(histo_output)
    plt.show()

def gammaCorrection(image, gamma=1):
    # Create a look-up table for gamma correction
    table = [((i / 255) ** gamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv.LUT(image, table)

menu()
option = int(input("\n**Enter your option: "))

while option !=0:
    #Read the input image
    if option == 1:
        img = cv.imread("KOKO4.jpg")
        cv.imshow("Koko's Image",img)
        cv.waitKey(0);

    #Convert the image into gray-scale
    elif option == 2:
        img_gary = cv.imread("KOKO4.jpg",cv.IMREAD_GRAYSCALE)
        cv.imshow("Koko in gray",img_gary)
        cv.waitKey(0);

    #Show the histogram of the image
    elif option == 3:
        img_gary = cv.imread("KOKO4.jpg",cv.IMREAD_GRAYSCALE)
        cv.imshow("Koko in gray",img_gary)   

        histo = cv.calcHist([img_gary],[0],None,[256],[0,256])

        plt.figure()
        plt.xlabel("Intensity")
        plt.ylabel("% of pixels")
        plt.xlim([0,256])
        plt.locator_params(axis='x', nbins=50)
        plt.locator_params(axis='y', nbins=20)
        plt.plot(histo)
        plt.show()
  
    #gamma correction using look up table 
    elif option == 4:
        #start time
        st = time.time()

        #random value of gamma
        gamma = random.uniform(0.01, 3.0)  
                          
        # original image
        img = cv.imread("KOKO4.jpg", cv.IMREAD_GRAYSCALE)
        # output image
        gammaImg = gammaCorrection(img, gamma)

        # concatenate the two images horizontally
        combined = np.concatenate((img, gammaImg), axis=1)
        # display the combined image
        cv.imshow('Before and After gamma ={}'.format(gamma), combined)

        #end time
        et = time.time()
        #execution time
        execution_time1 = et - st
        print("\nExecution time: {} seconds".format(execution_time1))

        #Histogram
        Histogram(img,gammaImg)

        cv.waitKey(0)
        cv.destroyAllWindows()

    #gamma correction without look up table 
    elif option == 5:
        #start time
        st = time.time()

        #random value of gamma
        gamma = random.uniform(0.01, 3.0)

        # original image
        img = cv.imread("KOKO4.jpg", cv.IMREAD_GRAYSCALE)

        #s = k * (r ^ gamma)
        k = 255 / np.float_power( np.max(img) , gamma)
        gammaImg = k* np.float_power(img , gamma)
        gammaImg = np.array(gammaImg , dtype='uint8' ) 

        # concatenate the two images horizontally
        combined = np.concatenate((img, gammaImg), axis=1)
        # display the combined image
        cv.imshow('Before and After gamma ={}'.format(gamma), combined)

        #end time
        et = time.time()
        #execution time
        execution_time2 = et - st
        print("\nExecution time: {} seconds".format(execution_time2))
                
        #Histogram
        Histogram(img,gammaImg)

        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("\nInvalid Option.")

    print()
    menu()
    option = int(input("\n**Enter your option: "))

print("Thanks for using this program :) ")