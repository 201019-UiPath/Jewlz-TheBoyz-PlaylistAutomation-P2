import os
import shutil
import sys
import time



def startPreprocessing(cwd, relative_path):

    input_datadir = relative_path + '/pre_img'
    output_datadir = relative_path + '/train_img'


    os.chdir(cwd + '/FaceRecognition/')
    if not hasattr(sys, 'argv'):
        sys.argv  = ['']
    sys.path.append('.')

    fullpath = os.path.expanduser(relative_path + '/pre_img/')
    if os.path.isdir(fullpath):
        shutil.rmtree(fullpath)
        time.sleep(.3) # making sure the folder is completely deleted before trying to create it again
        os.mkdir(fullpath)
  
    from preprocess import preprocesses

    obj = preprocesses(input_datadir,output_datadir)
    nrof_images_total, nrof_successfully_aligned = obj.collect_data()

    return 'Total number of images: {}. Number of successfully aligned images: {}'.format(nrof_images_total, nrof_successfully_aligned)
