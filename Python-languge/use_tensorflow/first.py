import tensorflow as tf
import numpy as np


# grader-required-cell

# GRADED FUNCTION: house_model
def house_model():
    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="MeanSquaredError")
    model.fit(xs, ys, epochs=1000)
    return model

model = house_model()
new_x = 7.0
prediction = model.predict([new_x])[0]
print(prediction)