import tensorflow as tf

from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.python.keras.utils.generic_utils import CustomObjectScope
from tensorflow import keras
from tensorflow.keras import backend as K
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)


def relu6(x):
    return K.relu(x, max_value=6)


def get_model():

    with CustomObjectScope({'relu6': relu6}):
        model = load_model('MobileNet_chest_abd_msk_Xray_extra_dense09-0.02.h5')

    return model


def evaluate(img):
    CATEGORIES = ["Abd_Xray", "Frontal_CXR", "Lateral_CXR", "MSK_Xray"]
    model = get_model()

    score = model.predict(img)

    print(score)
    return CATEGORIES[np.argmax(score)]
