from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import sys
from classifier import training

def startTraining(cwd):
    #os.chdir(cwd + '/FaceRecognition/')
    cwd = os.getcwd()
    os.chdir(cwd)
    if not hasattr(sys, 'argv'):
        sys.argv  = ['']
    sys.path.append('.')

    datadir = '~/OneDrive/Desktop/IdentificationModule/pre_img'
    modeldir = '~/OneDrive/Desktop/IdentificationModule/model/20170511-185253.pb'
    classifier_filename = '~/OneDrive/Desktop/IdentificationModule/class/classifier.pkl'
    print("Training Start")
    obj=training(datadir, modeldir, classifier_filename)
    print("Training Complete")
    get_file=obj.main_train()
    print('Saved classifier model to file "%s"' % get_file)
    return "Training completed."

