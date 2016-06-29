import numpy as np
import tensorflow as tf

batchSize = 5
imgSize = 3

data = np.reshape(np.arange(batchSize * (imgSize**2)),[batchSize,imgSize,imgSize])

coords = np.zeros((batchSize,2))
print coords

imgs = tf.Variable(data, name = 'images')
imgs = tf.cast(imgs, tf.int32)
coords = tf.Variable(coords, name = 'pixelCoordinates')

# kthCoord = tf.slice(imgs, [0,2,0], [batchSize,1,2])
# kthCoord = tf.reduce_sum(kthCoord, 1)

slice = tf.slice(imgs, [0,0,0], [5,1,1])

with tf.Session() as session:
    session.run(tf.initialize_all_variables())
    print(session.run(imgs))
    print(session.run(slice))


