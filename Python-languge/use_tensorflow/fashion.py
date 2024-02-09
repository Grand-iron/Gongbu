import keras.callbacks
import tensorflow as tf
import numpy as np
fmnist= tf.keras.datasets.fashion_mnist

(train_data,train_label),(test_data,test_lable)=fmnist.load_data()

train_data=train_data/255.0
test_data=test_data/255.0

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self,epochs,logs={}):
        if(logs.get('loss')<0.4):
            print("\n로스값이 0.4보다 작기에 작동을 중단합니다.")
            self.model.stop_training =True

class cola(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if(logs.get('accuracy')>0.85):
            print("\n어우 잘되네 친구")
            self.model.stop_training=True

callbacks = myCallback()

model=tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                  tf.keras.layers.Dense(128,activation=tf.nn.relu),
                                  tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(train_data,train_label,epochs=10,callbacks=[cola()])

model.evaluate(test_data, test_lable)

