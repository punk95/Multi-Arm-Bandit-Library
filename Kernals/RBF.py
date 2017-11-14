# Radial bias kernel

import tensorflow as tf


def RBF(a, b, zigma = 1, variance_weight = 1, datatype = "float64"):
    v1 = tf.Variable(a, dtype=tf.float64)
    v2 = tf.Variable(b, dtype=tf.float64)

    euclidian_dist = tf.reduce_sum(tf.square(tf.subtract(v1,v2)))
    ans = tf.exp(-0.5*euclidian_dist/zigma)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        answer = variance_weight*sess.run(ans)

    return answer