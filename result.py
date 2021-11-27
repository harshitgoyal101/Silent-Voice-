
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model('SV.model')
print(model.history.keys())