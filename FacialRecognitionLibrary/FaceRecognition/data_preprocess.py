import os
import shutil
import sys
import time



def startPreprocessing(cwd):

    input_datadir = '~/OneDrive/Desktop/IdentificationModule/pre_img'
    output_datadir = '~/OneDrive/Desktop/IdentificationModule/train_img'

    os.chdir(cwd + '/FaceRecognition/')
    if not hasattr(sys, 'argv'):
        sys.argv  = ['']
    sys.path.append('.')

    if os.path.isdir('C:\\Users\\jagib\\OneDrive\\Desktop\\IdentificationModule\\pre_img'):
        shutil.rmtree('C:\\Users\\jagib\\OneDrive\\Desktop\\IdentificationModule\\pre_img')
        time.sleep(.3) # making sure the folder is completely deleted before trying to create it again
        os.mkdir('C:\\Users\\jagib\\OneDrive\\Desktop\\IdentificationModule\\pre_img')

    from preprocess import preprocesses

    obj = preprocesses(input_datadir,output_datadir)
    nrof_images_total, nrof_successfully_aligned = obj.collect_data()

    return 'Total number of images: {}. Number of successfully aligned images: {}'.format(nrof_images_total, nrof_successfully_aligned)
