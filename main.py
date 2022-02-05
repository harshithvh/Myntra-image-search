#! python

# link for training dataset
# https://techlearn-cdn.s3.amazonaws.com/bs_myntra_image_search/myntra_train.zip

import numpy as np
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from sklearn.neighbors import NearestNeighbors
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Loading Dataset

train_dir = 'myntra_train/train/'
img_size = 224
batch_size = 64

img_gen_train = ImageDataGenerator(preprocessing_function = preprocess_input)
train_datagen = img_gen_train.flow_from_directory(train_dir,  #path to the parent folder
                                      target_size = (img_size, img_size), #size of the input image
                                      batch_size = batch_size, #size of the batches of data
                                      class_mode = None, #weather you want binary classes or categorical
                                      shuffle = False)

# Loading ResNet50

model = ResNet50(weights = 'imagenet', 
                 include_top = False,
                 input_shape = (img_size, img_size, 3),
                 pooling = 'max')

# Generating Product attributes (Features)

feature_list = model.predict(train_datagen)
# Get full path for all the images in our dataset
filenames = [train_dir + '/' + s for s in train_datagen.filenames]

# Using KNN on Product Features

neighbors = NearestNeighbors(n_neighbors = 3,
                             algorithm='ball_tree',
                             metric = 'euclidean')

print(neighbors.fit(feature_list))

#Pre-processing Image

img_path = 'test3.jpg'
input_shape = (img_size, img_size, 3) #Setting image size

img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1])) #Resizing image
img_array = image.img_to_array(img) #Converting it to an array
expanded_img_array = np.expand_dims(img_array, axis=0)
preprocessed_img = preprocess_input(expanded_img_array)

#Predicting similar images

test_img_features = model.predict(preprocessed_img, batch_size = 1)

_, indices = neighbors.kneighbors(test_img_features)

def similar_images(indices):
    plt.figure(figsize=(15,10), facecolor='white')
    plotnumber = 1    
    for index in indices:
        if plotnumber<=len(indices) :
            ax = plt.subplot(2,4,plotnumber)
            plt.imshow(mpimg.imread(filenames[index]), interpolation='lanczos')            
            plotnumber+=1
    plt.tight_layout()

plt.imshow(mpimg.imread(img_path), interpolation = 'lanczos')
plt.xlabel('Original Image',fontsize = 20)
plt.show()
print('Predictions for the Image ')
similar_images(indices[0])
plt.show()