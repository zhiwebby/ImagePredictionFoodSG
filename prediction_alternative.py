import tensorflow as tf
from PIL.ImageOps import crop
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization, Flatten
from tensorflow.keras.optimizers import Adam, Adamax
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras import regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, load_model, Sequential
import numpy as np
import pandas as pd
import shutil
import time
import cv2 as cv2
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import os
import seaborn as sns
sns.set_style('darkgrid')
from PIL import Image
from sklearn.metrics import confusion_matrix, classification_report
from IPython.core.display import display, HTML
from keras.utils.data_utils import get_file # download h5 keras model from github release
import flask
from flask import request # run a flask script
import time
# stop annoying tensorflow warning messages
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)

app = flask.Flask(__name__)

def print_in_color(txt_msg,fore_tupple,back_tupple,):
    #prints the text_msg in the foreground color specified by fore_tupple with the background specified by back_tupple
    #text_msg is the text, fore_tupple is foregroud color tupple (r,g,b), back_tupple is background tupple (r,g,b)
    rf,gf,bf=fore_tupple
    rb,gb,bb=back_tupple
    msg='{0}' + txt_msg
    mat='\33[38;2;' + str(rf) +';' + str(gf) + ';' + str(bf) + ';48;2;' + str(rb) + ';' +str(gb) + ';' + str(bb) +'m'
    print(msg .format(mat), flush=True)
    print('\33[0m', flush=True) # returns default print color to back to black
    return

def classify(sdir, csv_path,  model_path, crop_image = False):
    # read in the csv file
    class_df=pd.read_csv(csv_path)
    img_height=int(class_df['height'].iloc[0])
    img_width =int(class_df['width'].iloc[0])
    img_size=(img_width, img_height)
    scale=class_df['scale by'].iloc[0]
    try:
        s=int(scale)
        s2=1
        s1=0
    except:
        split=scale.split('-')
        s1=float(split[1])
        s2=float(split[0].split('*')[1])
        print (s1,s2)
    path_list=[]
    paths=os.listdir(sdir)
    for f in paths:
        path_list.append(os.path.join(sdir,f))

    print (' Model is being loaded- this will take about 10 seconds')
    model=load_model(model_path)
    image_count=len(path_list)
    index_list=[]
    prob_list=[]
    cropped_image_list=[]
    good_image_count=0
    for i in range (image_count):
        img=plt.imread(path_list[i])
        if crop_image == True:
            status, img=crop(img)
        else:
            status=True
        if status== True:
            good_image_count +=1
            img=cv2.resize(img, img_size)
            cropped_image_list.append(img)
            img=img*s2 - s1
            img=np.expand_dims(img, axis=0)
            p= np.squeeze (model.predict(img))
            index=np.argmax(p)
            prob=p[index]
            index_list.append(index)
            prob_list.append(prob)
    if good_image_count==1:
        class_name= class_df['class'].iloc[index_list[0]]
        probability= prob_list[0]
        img=cropped_image_list [0]
        """
        Comment off matplotlib in case
        """
        # plt.title(class_name, color='blue', fontsize=16)
        # plt.axis('off')
        # plt.imshow(img)
        return class_name, probability
    elif good_image_count == 0:
        return None, None
    most=0
    for i in range (len(index_list)-1):
        key= index_list[i]
        keycount=0
        for j in range (i+1, len(index_list)):
            nkey= index_list[j]
            if nkey == key:
                keycount +=1
        if keycount> most:
            most=keycount
            isave=i
    best_index=index_list[isave]
    psum=0
    bestsum=0
    for i in range (len(index_list)):
        psum += prob_list[i]
        if index_list[i]==best_index:
            bestsum += prob_list[i]
    img= cropped_image_list[isave]/255
    class_name=class_df['class'].iloc[best_index]
    """
    Comment off matplotlib in case
    """
    # plt.title(class_name, color='blue', fontsize=16)
    # plt.axis('off')
    # plt.imshow(img)
    return class_name, bestsum/image_count

# Write the Image File originating from Android App, write to "temp.jpg" in current directory
def uploadImageToDirectory(imageFile, imageFileName):
    picture = Image.open(imageFile)
    picture = picture.save(imageFileName)

"""
Create a function for storing in ~/storage.
"""
def uploadImageToStorage(img_path, store_path):
    img=cv2.imread(img_path)
    split=os.path.split(img_path)
    file_name=split[1]
    class_name=os.path.split(split[0])[1]
    full_name=class_name + '-' +file_name
    dst_path=os.path.join(store_path, full_name)
    cv2.imwrite(dst_path, img)
    return full_name

"""
Changed csv_path to github release
"""
# csv_path='class_dict.csv' # path to class_dict.csv
csv_path=get_file("class_dict.csv", "https://github.com/zhiwebby/ImagePredictionFoodSG/releases/download/v1.0.2/class_dict.csv")

"""
Changed model_path to github release
"""
#model_path='EfficientNetB2-nutricare-80.12.h5' # path to the trained model

# a function to download keras model extension(.h5) from URL and stock it in /app(current directory of heroku app)
# sample implementation : weights_path = get_file('the name under the model will be saved', 'YOUR URL')
model_path = get_file("EfficientNetB2-nutricare-86.12.h5", "https://github.com/zhiwebby/ImagePredictionFoodSG/releases/download/v1.0.2/EfficientNetB2-nutricare-86.12.h5")

@app.route('/', methods=['POST'])
def handle_request():
    # Calculate the duration of an operation
    start_time = time.monotonic()
    imageFile = request.files['image']

    """
    Creating storage directory in ~/storage.
    """
    working_dir  = os.getcwd()
    store_path=os.path.join(working_dir, 'storage')
    if os.path.isdir(store_path):
        shutil.rmtree(store_path)
    os.mkdir(store_path)

    """
    Changed img_path to temp
    """
    # img_path='whiskey.jpg'
    img_path='temp.jpg'

    """
    Upload image to directory
    """
    uploadImageToDirectory(imageFile, img_path)
    full_name = uploadImageToStorage(img_path, store_path)
    # check if the directory was created and image stored
    print (os.listdir(working_dir))

    class_name, probability=classify(store_path, csv_path,  model_path, crop_image = False) # run the classifier
    msg=f'image {full_name} is of {class_name} with a probability of {probability * 100: 6.2f} %'
    """
    Comment off msg
    """
    # print_in_color(msg, (0,255,255), (65,85,55))
    print(msg)
    os.remove(img_path)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)
    return msg

if __name__=="__main__":
    app.run(debug=True)