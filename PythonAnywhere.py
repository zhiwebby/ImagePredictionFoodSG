#!/usr/bin/python3.7
#!/home/zhiwebby1/.virtualenvs/my-virtualenv
import flask
from flask import request
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
import tensorflow as tf
import os
from tensorflow.keras.models import load_model
from PIL import Image
import PIL
import time
from keras.utils.data_utils import get_file

app = flask.Flask(__name__)

# grabs the labels.txt file to create list of foods
def create_foodlist(path):
    list_ = list()

    with open(path, 'r') as txt:
        foods = [read.strip() for read in txt.readlines()]
        for f in foods:
            list_.append(f)
            #print("Appended food - " + f)
    return list_

# retrieving the abs path of the model / labels / flask python script
basepath = os.path.abspath(".")
# basepath = "/home/zhiwebby/mysite"

print("basepath: ", basepath)

# a function to download keras model extension(.h5) from URL and stock it in /app(current directory of heroku app)
# sample implementation : weights_path = get_file('the name under the model will be saved', 'YOUR URL')
model_downloaded_path = get_file("EfficientNetB2-nutricare-80.12.h5", "https://github.com/zhiwebby/ImagePredictionFoodSG/releases/download/v1.0/EfficientNetB2-nutricare-80.12.h5")

# loading the model that was trained and fine-tuned
# Commented out older models
# MN_model = load_model(basepath + "/MN_model_trained.pb", compile = False)
# EFN_model = load_model(basepath + "/EfficientNetB2-nutricare-99.11.pb", compile = False)
# EFN_model = load_model(basepath + "/EfficientNetB2-nutricare-80.12.pb", compile = False)
# Loading the h5 to prevent Tensorflow backend from causing a dyno timeout after 30 seconds
EFN_model = load_model(model_downloaded_path, compile = False)

# food_list = create_foodlist(basepath + "/foodsg/meta/labels.txt")
food_list = create_foodlist(basepath + "/foodsg_for_431_labels/meta/labels.txt")

food_image_for_recognition = basepath + "/temp.jpg"

# Write the Image File originating from Android App, write to "temp.jpg" in current directory
def uploadImageToDirectory(imageFile):
    picture = Image.open(imageFile)
    picture = picture.save(food_image_for_recognition)

# Predict for MobileNet
def predict_class(model, imageFile, size, show = True):
    print("uploadImageToDirectory")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    # Upload image for recognition as temp.jpg in current directory
    uploadImageToDirectory(imageFile)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("image.load_img")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    # Tensorflow retrieve temp.jpg from current directory
    loadImage = image.load_img(food_image_for_recognition, target_size=(size, size))
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("os.remove")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    # Delete temp.jpg to free up disk space
    os.remove(food_image_for_recognition)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("image.img_to_array")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    img = image.img_to_array(loadImage)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("np.expand_dims")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    img = np.expand_dims(img, axis=0)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("calculation")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    img /= 255.
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)

    print("model.predict")
    # Calculate the duration of an operation
    start_time = time.monotonic()
    pred = model.predict(img)
    # Calculate the duration of an operation
    print('seconds: ', time.monotonic() - start_time)
    print("np.argmax")
    index = np.argmax(pred)    # Returns the indices of the maximum values along an axis, In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned.
    print("food_list.sort")
    food_list.sort()
    print("food_list[index]")
    pred_value = food_list[index]
    print("tf.nn.softmax")
    score = tf.nn.softmax(pred)

    # printing % chance of food

    # print(np.max(score))    # chance is still very low (4%) even if top-5 is accurate. may be good enough?
    # print(np.min(score))    # least likely food chance. should be a significant % smaller than the max.

    # this chance seems small but note that the matrix array has % chance of EVERY SINGLE other food in the class.

    # does this mean it gets worse when we add more classes? will find out when doubling the dataset with other data

    # return predicted food name as the first index in array
    array_results = [food_list[index], str(np.max(score)), str(np.min(score))]
    return array_results


# Predict for EfficientNet
def predict_class_for_EFN_model(model, imageFile, size, size2, show = True):

    # Upload image for recognition as temp.jpg in current directory
    uploadImageToDirectory(imageFile)
    # Tensorflow retrieve temp.jpg from current directory
    loadImage = image.load_img(food_image_for_recognition, target_size=(size, size2))
    # Delete temp.jpg to free up disk space
    os.remove(food_image_for_recognition)
    img = image.img_to_array(loadImage)
    img = np.expand_dims(img, axis=0)
    img /= 255.

    pred = model.predict(img)
    index = np.argmax(pred)    # Returns the indices of the maximum values along an axis, In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned.
    food_list.sort()
    pred_value = food_list[index]

    score = tf.nn.softmax(pred)

    # printing % chance of food

    # print(np.max(score))    # chance is still very low (4%) even if top-5 is accurate. may be good enough?
    # print(np.min(score))    # least likely food chance. should be a significant % smaller than the max.

    # return predicted food name as the first index in array
    array_results = [food_list[index], str(np.max(score)), str(np.min(score))]
    return array_results

    # this chance seems small but note that the matrix array has % chance of EVERY SINGLE other food in the class.

    # does this mean it gets worse when we add more classes? will find out when doubling the dataset with other data

@app.route('/', methods=['POST'])
def handle_request():
    imageFile = request.files['image']

    # MobileNetV2 will not be tested because of testing EfficientNet that Zhi Wen crawled
    # print("Predicting using MobileNetV2")
    #
    # array_results_for_MN_model = predict_class(MN_model, imageFile, 299, True)

    print("Predicting using EfficientNetB2")

    array_results_for_EFN_model = predict_class_for_EFN_model(EFN_model, imageFile, 224, 306, True)

    # trying different syntax to get results

    uploadImageToDirectory(imageFile)
    img = tf.keras.preprocessing.image.load_img(food_image_for_recognition, target_size=(224,306))
    os.remove(food_image_for_recognition)
    input_arr = keras.preprocessing.image.img_to_array(img)

    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = EFN_model.predict(input_arr)

    score = tf.nn.softmax(predictions[0])

    return "This image most likely belongs to {}".format(array_results_for_EFN_model[0])

if __name__=="__main__":
    app.run(debug=True)