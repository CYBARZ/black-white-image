
import cv2 as cv , cv2
import os
import numpy as np
import argparse
from os.path import isfile, join



def color(input_image_path):

    
    #make main folder
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')

    try:
        if not os.path.exists('data/colored'):
            os.makedirs('data/colored')
    except OSError:
        print ('Error: Creating directory of data')    

    print("yes it is working")
    caffemodel = "model\colorization.caffemodel"
    prototxt = "model\colorization_deploy_v2.prototxt"
    kernel = "model\pts_in_hull.npy"
    print("models called successfully")


    
        
 

    inp = input_image_path   

        
    # Network input size
    W_in = 224
    H_in = 224
    imshowSize = (640, 480)


    # Create network graph and load weights
    net = cv.dnn.readNetFromCaffe(prototxt, caffemodel)
    # load cluster centers
    pts_in_hull = np.load(kernel)
    # populate cluster centers as 1x1 convolution kernel
    pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
    net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
    net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]


    print(inp)
    # Read the input image in BGR format
    frame = cv.imread(inp)
               
               
    # convert it to rgb format
    frame = frame[:, :, [2, 1, 0]]
    # Scale the image to handle the variations in intensity
    img_rgb = (frame * 1.0 / 255).astype(np.float32)
    # convert to Lab color space
    img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
    # pull out L channel
    img_l = img_lab[:, :, 0]
    (H_orig, W_orig) = img_rgb.shape[:2]  # original image size

    # resize image to network input size
    img_rs = cv.resize(img_rgb, (W_in, H_in))  # resize image to network input size
    img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
    img_l_rs = img_lab_rs[:, :, 0]
    # subtract 50 for mean-centering
    img_l_rs -= 50


    # Set the input for forwarding through the openCV DNN module
    net.setInput(cv.dnn.blobFromImage(img_l_rs))

    # Inference on network
    ab_dec = net.forward('class8_ab')[0, :, :, :].transpose((1, 2, 0))  # this is our result
     # Get the a and b channels
    (H_out, W_out) = ab_dec.shape[:2]
     # Resize to original size
    ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
    # concatenate with original image i.e. L channel
    img_lab_out = np.concatenate((img_l[:, :, np.newaxis], ab_dec_us), axis=2)
     # convert to BGR space from Lab space
    img_bgr_out = cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR)
    # Clip and then rescale to 0-255
    img_bgr_out = 255 * np.clip(img_bgr_out, 0, 1)
    img_bgr_out = np.uint8(img_bgr_out)
    # concatenate input and output image to display
    con = np.hstack([frame, img_bgr_out])
    print("everything")
    cv.imwrite('.\data\colored\out' + inp, img_bgr_out)
    cv.imshow("subash",img_bgr_out)
    #os.remove(input_image_path)
