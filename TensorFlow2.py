import tensorflow as tf

edges = tf.constant([[0, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0]], dtype=tf.int32)
mat1 = tf.zeros((4, 4), dtype=tf.int32)

# Building the edge condition matrix:
edges_bool = tf.equal(edges, 1)  # edges[:, :] == 1

edges_cond_i = edges_bool[:, 0]  # edges[:, 0] == 1
edges_cond_i = tf.tile(tf.expand_dims(edges_cond_i, 1), (1, 4))
edges_cond_j = edges_bool[0, :]  # edges[0, :] == 1
edges_cond_j = tf.tile(tf.expand_dims(edges_cond_j, 0), (4, 1))
edges_cond_ij = tf.logical_and(edges_cond_i, edges_cond_j)
# edges[:, 0] == 1 and edges[0, :] == 1
edges_cond = tf.logical_or(edges_bool, edges_cond_ij)
# edges[:, :] == 1 or (edges[:, 0] == 1 and edges[0, :] == 1)

# Applying the condition to mat1:
ones = tf.ones((4, 4), dtype=tf.int32)
mat1 = tf.where(edges_cond, ones, mat1)

# Displaying results:
with tf.device('/cpu:0'), tf.Session() as sess:
    res = sess.run(mat1)
    print(res)
