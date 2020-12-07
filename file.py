import numpy as np
import os
import cv2

"""
    read two data files and return array representation ( 'model.data' , 'extrinsic.xml' )
"""
def read(baseDir):
    model, extrinsic = [],[]
    for file in os.listdir(baseDir):
        if file.endswith('.data'):
            path = os.path.join(baseDir, file)
            model = readData(path)
        elif file.endswith('.xml'):
            path = os.path.join(baseDir, file)
            extrinsic = readXML(path)
    return model, extrinsic

"""
    read xml file storing extrinsic parameter each board
"""
def readXML(filepath, camIndex = 1):
    fs = cv2.FileStorage(filepath, cv2.FILE_STORAGE_READ)
    extrinsic = []
    a = range(0,5)
    for i in a:
        extrinsic.append(fs.getNode('Extrinsic_' + str(i)).mat())

    return extrinsic

"""
    read data file storing checkerboard absolute position
"""
def readData(filepath):
    model = []
    point = []
    with open(filepath) as f:
        for line in f:
            line = line.strip().split()
            for item in line:
                point.append(float(item))
                if len(point) == 2:
                    model.append(point)
                    point = []

    return model
