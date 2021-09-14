import os
import re

import numpy as np
from PIL import Image
from tensorflow.keras.utils import to_categorical


def load_data(image_dir):
    """Load the MNIST-digit images and labels from a given path."""

    image_names = os.listdir(image_dir)
    N = len(image_names)

    # List of images.
    X = np.empty((N, 28, 28, 1))
    # List of labels.
    y = np.empty((N,))

    """
    Regex to extract the label from the filename.

    Filenames are of the form UniqueId_Label.png where UniqueId is just a unique number identifying an image
    and Label is the digit that is represented in the image.
    """
    label_regex = re.compile(r"\d+_(\d)")

    for i, image_name in enumerate(image_names):
        # Load the image.
        image_path = os.path.join(image_dir, image_name)
        image = Image.open(image_path)
        # Get the label.
        label = label_regex.match(image_name)[1]

        # Convert from image file to array.
        image_array = np.asarray(image)
        image_array = image_array.astype('float32')
        # Normalize all values to [0; 1)
        image_array = image_array / 255

        # Add sample to the list.
        X[i, ...] = np.expand_dims(image_array, axis=-1)
        y[i] = int(label)

    """
    This functions performs what is called "one-hot encoding".

    It's a standard way to represent categorical data in Machine Learning. If our data can be one of N classes
    then we will represent the n-th label as a vector of length N with all 0 values except for the n-th which will be 1.
    This is doen because the model can only predict numerical values and labels are not (strictly) numerical.

    Example
    If the classes are ["cat", "dog", "table"] then N = 3
    "cat" => [1, 0, 0]
    "dog" => [0, 1, 0]
    "table" => [0, 0, 1]

    You can read more about it here:
    https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/
    https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/
    """
    y = to_categorical(y)

    return X, y


def load_dataset(data_dir):
    """Load both training and testing data."""

    train_dir = os.path.join(data_dir, "training")
    test_dir = os.path.join(data_dir, "testing")

    X_train, y_train = load_data(train_dir)
    X_test, y_test = load_data(test_dir)

    return (X_train, y_train), (X_test, y_test)
