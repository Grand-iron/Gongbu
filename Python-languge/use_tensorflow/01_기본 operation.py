import tensorflow as tf

@tf.function          #함수 지정 
def adder(a,b):
    return a+b

q=tf.constant(1)      #constant = 설정
x=tf.constant(2)


tf.print(adder(q,x))